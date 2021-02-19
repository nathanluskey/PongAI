from agent import Agent
from pongEnvironment import PongEnvironment

class Game():
    __innit__(self, qTable=dict()):
        self.currentAgent = agent(qTable=)



if __name__ == "__main__":
    universalQTable = dict()

    currentAgent = agent(qTable=universalQTable)
    game = pongEnviroment()

    while (not (game.isTerminal())):
        # Play a game
        currentState = game.getCurrentState()
        actions = game.getPossibleActions()
        actionPicked = currentAgent.pickAction(currentState, actions)
        reward = game.doAction(actionPicked)
        print("Reward: {}, Action Picked: \n{}".format(reward, actionPicked))
        futureState = game.getCurrentState()
        futureActions = game.getPossibleActions()
        currentAgent.updateQTable(currentState, actionPicked, reward, futureState, futureActions)
    
    universalQTable = currentAgent.qTable
    print(universalQTable)
    