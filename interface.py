from agent import Agent
from pongEnvironment import PongEnvironment

class Game:
    def __init__(self, verbose=False, qTable=dict(), radiusOfShooting=0):
        self.agent = Agent(qTable=qTable)
        self.game = PongEnvironment(radiusOfShooting=radiusOfShooting)
        self.verbose = verbose
        self.shotsTaken = 0

    def playGame(self):
        while (not (self.game.isTerminal())):
            self.shotsTaken += 1
            currentState = self.game.getCurrentState()
            actions = self.game.getPossibleActions()
            actionPicked = self.agent.pickAction(currentState, actions)
            reward = self.game.doAction(actionPicked)
            if (self.verbose):
                print("Reward: {}, Action Picked: \n{}".format(reward, actionPicked))
            futureState = self.game.getCurrentState()
            futureActions = self.game.getPossibleActions()
            self.agent.updateQTable(currentState, actionPicked, reward, futureState, futureActions)
    
    def getQTable(self, normalize=True):
        if (normalize):
            # Normalize the qTable returned to avoid huge runaways
            qTableCopy = self.agent.qTable.copy()
            maxQ = -1
            for key in qTableCopy.keys():
                currQ = self.agent.qTable[key]
                if (currQ > maxQ):
                    maxQ = currQ
            for key in qTableCopy.keys():
                qTableCopy[key] = qTableCopy[key] / maxQ
            return qTableCopy
        else:
            return self.agent.qTable

    def getShotsTaken(self):
        return self.shotsTaken

if __name__ == "__main__":
    game = Game(verbose=True)
    game.playGame()
    print(game.getQTable())
    