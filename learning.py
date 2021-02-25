from interface import Game
import pickle
import time
import numpy as np
import pandas as pd
import os

# Create a universal Q-Table
universalQTable = dict()
gamesToPlay = 10000
radiiOfShooting = np.arange(0, 2.75, 0.25)
allShotsTaken = np.zeros(gamesToPlay)
for radiusOfShooting in radiiOfShooting:
    tic = time.perf_counter()
    for i in range(gamesToPlay):
        print("Playing Game #{}".format(i), end="\r")
        currentGame = Game(qTable=universalQTable, radiusOfShooting=radiusOfShooting)
        currentGame.playGame()
        universalQTable = currentGame.getQTable()
        # If you want to know how many shots were taken uncomment the following line
        # allShotsTaken[i] = currentGame.getShotsTaken()

    toc = time.perf_counter()
    print("It took {:0.2f}s to run {} simulations with radius {:0.2f}!".format((toc - tic), gamesToPlay, radiusOfShooting))

    # Export the Q-Table to a pickle
    fileName = "rawTable_{:0.2f}.p".format(radiusOfShooting)
    fullPath = os.path.join("./rawTables", fileName)
    with open(fullPath, "wb") as filePointer:
        pickle.dump(universalQTable, filePointer)

