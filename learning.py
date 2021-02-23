from interface import Game
import pickle
import time
import numpy as np
import pandas as pd

# Create a universal Q-Table
universalQTable = dict()
gamesToPlay = 100000
radiusOfShooting = 1
allShotsTaken = np.zeros(gamesToPlay)

tic = time.perf_counter()
for i in range(gamesToPlay):
    print("Playing Game #{}".format(i), end="\r")
    currentGame = Game(qTable=universalQTable, radiusOfShooting=radiusOfShooting)
    currentGame.playGame()
    universalQTable = currentGame.getQTable()
    allShotsTaken[i] = currentGame.getShotsTaken()

toc = time.perf_counter()
print("It took {:0.2f}s to run {} simulations!".format((toc - tic), gamesToPlay))

# Export the Q-Table to a pickle
with open("sampleTable.p", "wb") as filePointer:
    pickle.dump(universalQTable, filePointer)

# ExporT the shotsTaken to a csv
shotsTakenData = pd.DataFrame(data=allShotsTaken)
shotsTakenData.to_csv("shotsTaken_{}_{}.csv".format(radiusOfShooting, gamesToPlay))

