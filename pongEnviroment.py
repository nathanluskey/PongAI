from environment import Environment
import numpy as np


class pongEnviroment(Environment):
    def __init__(self, radiusOfShooting=1):
        # TODO: Create a local variable of the current cups layout and how many re-racks have been used
        # TODO: Incoroporate the radius of shooting to be how accurate someone is, roughly
        self.currentState = np.array() #TODO: FIll THIS IN
    
    def getCurrentState(self):
        # TODO: write out a doc explaining this
        return self.currentState

    def getPossibleActions(self):
        # TODO: Yea... this one is going to be fun... I think return position of each cup and if a re-rack can take place
        cupsLeft = self.currentState.sum()

        if (cupsLeft == 2):
            # TODO: Change this to push both cups to the back by default in self.currentState
            pass
        elif (cupsLeft == 3):
            # TODO: This will be the 2(?) the ways 3 cups will be arranged
            pass
        elif (cupsLeft == 6):
            # TODO: Figure this out...
            pass


    def doAction(self, action):
        # TODO: Check if action is a re-rack, and do this with updating the state
        # TODO: With some likelyhood hit a cup or surrounding cups, this is dependent on the radiusOfShooting
        pass

    def isTerminal(self):
        # TODO: Check if there is 1 cup left. For our purposes this is our goal.
        pass
