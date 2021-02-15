from environment import Environment
import numpy as np

class stateOfGame():
    def __init__(self):
        self.reracks = 0
        self.totalReracks = 3
        self.cups = np.zeros(28, dtype=np.int8)
        self.cups[[3, 9, 11, 15, 17, 19, 21, 23, 25, 27]] = 1
    
    def getCups(self):
        return self.cups

    def getNumCups(self):
        return self.cups.sum()

    def useRerack(self):
        self.reracks += 1

    def canRerack(self):
        return self.reracks < self.totalReracks

class pongEnviroment(Environment):
    def __init__(self, radiusOfShooting=1):
        # Create a local variable of the current cups layout and how many re-racks have been used
        self.currentState = stateOfGame()
        # Incoroporate the radius of shooting to be how accurate someone is, roughly
        self.radiusOfShooting = radiusOfShooting
    
    def getCurrentState(self):
        # TODO: write out a doc explaining this
        pass

    def getPossibleActions(self):
        actions = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
        cupsLeft = self.currentState.getNumCups()
        # Checking if reracks are allowed
        if (self.currentState.canRerack()):
            if (cupsLeft == 3):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[10, 17, 24]] = 1
                actions = np.vstack((actions, newState))
            elif (cupsLeft == 4):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[16, 17, 23, 24]] = 1
                actions = np.vstack((actions, newState))
            elif (cupsLeft == 6):
                newState = np.zeros(self.currentState.getCups().shape, dtype=self.currentState.getCups().dtype)
                newState[[10, 16, 18, 22, 24, 26]] = 1
                actions = np.vstack((actions, newState))
        # Add all permuations of currentState
        cupPositions = self.currentState.getCups().nonzero()[0]
        for cupPosition in cupPositions:
            newState = self.currentState.getCups().copy()
            newState[cupPosition] = 0
            actions = np.vstack((actions, newState))

        actions = actions[1:, :] #Get rid of first entry which was just all zeros
        return actions

    def doAction(self, newState):
        # TODO: Check if action is a re-rack, and do this with updating the state, and USING A RERACK
	    
        # TODO: With some likelyhood hit a cup or surrounding cups, this is dependent on the radiusOfShooting
        
        # If there are only 2 cups left, then move them to the final configuration
        pass
            

    def isTerminal(self):
        # Check if there is 1 cup left. For our purposes this is our goal.
        return self.currentState.getNumCups() == 1
