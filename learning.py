from interface import Game
import pickle
import time
import numpy as np
import pandas as pd
import os

"""
def hasPolicyChanged(previousPolicy, newPolicy, triggeringDifference=0.25):
    # Check either policy is empty
    if (not previousPolicy or not newPolicy):
        return True
    else:
        # Check if they have the same number of keys
        if (len(previousPolicy) != len(newPolicy)):
            return True
        else:
            allDifferences = np.zeros(len(newPolicy))
            i = 0
            for newPolicyKey in newPolicy.keys():
                difference = newPolicy[newPolicyKey] - previousPolicy.get(newPolicyKey, 0)
                allDifferences[i] = difference
                i = i + 1
            meanDifference = np.mean(allDifferences)
            if (meanDifference > triggeringDifference):
                return False
            else:
                return True
"""
def calculateEpsilon(initialEpsilon, gamesPlayed):
    outputEpsilon = initialEpsilon * np.exp(-1E-5 * gamesPlayed)
    return outputEpsilon


# Create a universal Q-Table
universalQTable = dict()
gamesToPlay = 50000
radiiOfShooting = np.arange(0, 3, 0.5)
# allShotsTaken = np.zeros(gamesToPlay)
initialEpsilon = 0.9

for radiusOfShooting in radiiOfShooting:
    tic = time.perf_counter()
    for i in range(gamesToPlay):
        currentEpsilon = calculateEpsilon(initialEpsilon, i)
        print("Epsilon = {:0.4f}, Playing Game #{}".format(currentEpsilon, i), end="\r")
        currentGame = Game(qTable=universalQTable, radiusOfShooting=radiusOfShooting, epsilon=currentEpsilon)
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

"""
universalQTable = dict()
previousUniversialQTable = dict()
radiiOfShooting = np.arange(0, 3, 0.5)
minimumGamesToPlay = 10000
initialEpsilon = 0.9

for radiusOfShooting in radiiOfShooting:
    gamesPlayed = 0
    tic = time.perf_counter()
    # Play as many games until the policy is basically in it's final form
    while (gamesPlayed < minimumGamesToPlay or hasPolicyChanged(previousUniversialQTable, universalQTable)):
        currentEpsilon = calculateEpsilon(initialEpsilon, gamesPlayed)
        print("Epsilon = {:0.4f}, Playing Game #{}".format(currentEpsilon, gamesPlayed), end="\r")
        currentGame = Game(qTable=universalQTable, radiusOfShooting=radiusOfShooting, epsilon=currentEpsilon)
        currentGame.playGame()
        previousUniversialQTable = universalQTable
        universalQTable = currentGame.getQTable()
        gamesPlayed = gamesPlayed + 1
    
    toc = time.perf_counter()
    print("It took {:0.2f}s to run {} simulations with radius {:0.2f}!".format((toc - tic), gamesPlayed, radiusOfShooting))
    
    # Export the Q-Table to a pickle
    fileName = "rawTable_{:0.2f}.p".format(radiusOfShooting)
    fullPath = os.path.join("./rawTables", fileName)
    with open(fullPath, "wb") as filePointer:
        pickle.dump(universalQTable, filePointer)

"""