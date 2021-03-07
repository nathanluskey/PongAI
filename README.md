# [PongAI](https://nathanluskey.github.io/PongAI/)
 This project is about learning to play pong using reinforcement learning. The specific method used is *epsilon-greedy Q-learning* which I'll explain a little more. I will also talk about the actual code implimentation.

## The Basics of Reinforcement Learning
![RL Diagram](https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg)
The basic interaction is that an *enviroment* specifies *actions* with the agent then picking an action and recieving some *reward*. Now there's the question: **How does the agent make a well informed decision of the best action to pick given the current state of the enviroment?**

 ### Q-Learning
 Q-Learning is a method for creating an agent that makes an informed decision. It boils down to the agent trying different actions, seeing the reward, then estimating the *utility* of each action in the state. Estimating the utility is done using this equation:
 ![Q Learning EQ](https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686)

 As the agent learns, it builds up a *policy* which is an estimation of the utility of each action in each state based off experience. Now we need a way of balancing *exploration* and *explotation*, so that we can ideally have on an optimal policy at the end of the day.

 ### What's Epsilon-Greedy?
Episolon Greedy is a simply that with some chance epsilon (0-1) the agent picks a random action instead of following the best action from the policy. This leads to the agent exploring. As the agent explores more, it starts to build a coherent policy, so it can start to exploit the policy picking the optimal action. This is why I made the epsilon decrease exponentially with the number of games played.


 ## Implimentation
Theory aside, let's talk implimentation. I wrote the bulk of the code in Python using numpy because [numpy is really fast](https://www.geeksforgeeks.org/why-numpy-is-faster-in-python/). The code for the enviroment is in ```pongEnviroment.py``` and running the command ```python pongEnviroment.py``` will let you manually play a game in the command line. The enviroment has stochastisticy built in with there being a *radiusOfShooting*; this is a normally distributed shooting radius centered at whichever cup was chosen to be the target. The agent is ```agent.py``` and the interface between the two is in ```interface.py```. The training is all in ```learning.py``` where 50,000 games are played with varying radii from 0-2.5. The script outputs several pickle files into the rawTables folder. 

Now, we move on to actually visualizing these policies. I decided to use githubs static website hosting because it's free and I know basic html/css/javascript well enough. The ```processPickles.py``` script takes each of the raw tables, and turns them into a massive json of colors for each cup given a state. This is then popped into the docs folder with the html, javascript, and some css to make the front end visualization. Feel free to explore this at [https://nathanluskey.github.io/PongAI/](https://nathanluskey.github.io/PongAI/). 

## Final Notes
I started on this project because I thought it would be interesting and I couldn't find similar examples online. Pong is fairly ideal for q-learning due to the rigid way of describing states and ability to build out a table to describe all state-action pairs. 