import numpy as np

class agent:
    def __init__(self, qTable=dict(), learningRate=0.5, discountFactor=0.5, epsilon=0.25):
        self.qTable = qTable
        self.learningRate = learningRate
        self.discountFactor = discountFactor
        self.epsilon = epsilon

    def pickAction(self, currentState, actions):
        outputAction = None
        # Epsilon Greedy method for picking an action
        if (np.random.random_sample() <= self.epsilon):
            # pick a random action
            actionIndex = np.random.random_integers(0, high=(actions.shape[2] - 1))
            outputAction = actions[:, :, actionIndex]
        else:
            # pick the max Q action
            highestQ = -1
            for actionIndex in range(actions.shape[2]):
                action = actions[:, :, actionIndex]
                key = self.makeKey(currentState, action)
                qValue = self.qTable.get(key, 0) #Default to 0
                if (qValue > highestQ):
                    # Make this action the action to do
                    highestQ = qValue
                    outputAction = action
                elif (qValue == highestQ):
                    # Make it a 50/50 shot of doing this action
                    if (np.random.random_sample() < 0.5):
                        outputAction = action
                 
        return outputAction

    def updateQTable(self, currentState, action, reward, futureState, futureActions):
        # TODO: Update q table values
        # https://en.wikipedia.org/wiki/Q-learning
        key = self.makeKey(currentState, action)
        currentUtility = self.qTable.get(key, 0)
        pass

    def makeKey(self, state, action):
        key = np.hstack((state, action)).flatten()
        key = tuple(key)
        return key