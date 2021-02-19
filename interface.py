from agent import Agent
from pongEnvironment import PongEnvironment

class Game:
    def __init__(self, verbose=False, qTable=dict(), radiusOfShooting=0):
        self.agent = Agent(qTable=qTable)
        self.game = PongEnvironment(radiusOfShooting=radiusOfShooting)
        self.verbose = verbose

    def playGame(self):
        while (not (self.game.isTerminal())):
            currentState = self.game.getCurrentState()
            actions = self.game.getPossibleActions()
            actionPicked = self.agent.pickAction(currentState, actions)
            reward = self.game.doAction(actionPicked)
            if (self.verbose):
                print("Reward: {}, Action Picked: \n{}".format(reward, actionPicked))
            futureState = self.game.getCurrentState()
            futureActions = self.game.getPossibleActions()
            self.agent.updateQTable(currentState, actionPicked, reward, futureState, futureActions)
    
    def getQTable(self):
        return self.agent.qTable


if __name__ == "__main__":
    game = Game(verbose=True)
    game.playGame()
    print(game.getQTable())
    