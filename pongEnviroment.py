from environment import Environment
import numpy as np

class stateOfGame():
    def __init__(self):
        self.reracks = 0
        self.totalReracks = 3
        self.cups = np.zeros((4, 7), dtype=np.int8)
        self.cups[[0, 1, 1, 2, 2, 2, 3, 3, 3, 3], [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]] = 1
    
    def getCups(self):
        return self.cups
    
    def setCups(newCups, self):
        self.cups = newCups

    def getNumCups(self):
        return self.cups.sum()

    def useRerack(self):
        self.reracks += 1

    def canRerack(self):
        return self.reracks < self.totalReracks

class pongEnviroment(Environment):
    def __init__(self, radiusOfShooting=0, cupReward=5):
        # Create a local variable of the current cups layout and how many re-racks have been used
        self.currentState = stateOfGame()
        # Incoroporate the radius of shooting to be how accurate someone is, roughly
        self.radiusOfShooting = radiusOfShooting
        self.cupReward = cupReward
    
    def getCurrentState(self):
        output = dict()
        output["cups"] = self.currentState.getCups()
        output["reracks"] = self.currentState.reracks
        return output

    def getPossibleActions(self):
        actions = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
        cupsLeft = self.currentState.getNumCups()
        # Checking if reracks are allowed
        if (self.currentState.canRerack()):
            if (cupsLeft == 3):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[1, 2, 3], [3, 3, 3]] = 1
                actions = np.dstack((actions, newState))
            elif (cupsLeft == 4):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[2, 2, 3, 3], [2, 3, 2, 3]] = 1
                actions = np.dstack((actions, newState))
            elif (cupsLeft == 6):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[1, 2, 2, 3, 3, 3], [3, 2, 4, 1, 3, 5]] = 1
                actions = np.dstack((actions, newState))
        
        # Add all permuations of currentState
        cupPositions = self.currentState.getCups().nonzero()
        for i in range(len(cupPositions[0])):
            newState = self.currentState.getCups().copy()
            newState[cupPositions[0][i], cupPositions[1][i]] = 0
            actions = np.dstack((actions, newState))

        actions = actions[:, :, 1:] #Get rid of first entry which was just all zeros
        return actions

    def doAction(self, newState):
        reward = 0
        if (newState.sum() == self.currentState.getNumCups()):
            self.currentState = newState
            self.currentState.useRerack()
        else:
            # TODO: With some likelyhood hit a cup or surrounding cups, this is dependent on the radiusOfShooting
            # Figure out what cup is being aimed for
            cupAimedFor = self.currentState.getCups() - newState
            row = cupAimedFor[0][0]
            column = cupAimedFor[1][0]
            # Add a normally distributed random variable to each index and round it
            row = np.round((np.random.normal(loc=row, scale=self.radiusOfShooting)))
            column = np.round((np.random.normal(loc=column, scale=self.radiusOfShooting)))
            row = row.astype(np.int8)
            column = column.astype(np.int8)
            # Check if we this is a valid index
            if ((row >= 0 and row < self.currentState.getCups().shape[0]) and (column >= 0 and column < self.currentState.getCups().shape[1])):
                newState = self.currentState.getCups().copy()
                newState[row, column] = 0
                # Check if we hit something (anything!)
                if ((self.currentState.getCups() - newState).sum() != 0):
                    reward = self.cupReward
                    self.currentState.setCups(newState)

        # If there are only 2 cups left, then move them to the final configuration
        if (self.currentState.getNumCups() == 2):
            newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
            newState[[2, 3], [3, 3]] = 1
            self.currentState = newState 

        return reward
            

    def isTerminal(self):
        # Check if there is 1 cup left. For our purposes this is our goal.
        return self.currentState.getNumCups() == 1