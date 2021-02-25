import numpy as np
import pickle
import os
import json

def getRow(stateMatrix, actionMatrix):
    # Given an the input state and action, output the index to be modified
    outputIndex = None
    if (stateMatrix.sum() == actionMatrix.sum()):
        # This is a re-rack
        outputIndex = 16
    else:
        cupAimedFor = (stateMatrix - actionMatrix).nonzero()
        row = cupAimedFor[0][0]
        column = cupAimedFor[1][0]
        if (row == 0):
            outputIndex = 0
        elif (row == 1):
            outputIndex = column - 1
        elif (row == 2):
            outputIndex = column + 3
        elif (row == 3):
            outputIndex = column + 9
    return outputIndex

def getColumn(stateMatrix):
    # Given an input state, return what column this goes into
    # This is going to be a bit convoluted, but doing 2^getRow(currentState, (currentState - 1 cup))
    # Then for each 
    cupPositions = stateMatrix.nonzero()
    outputIndex = 0
    for i in range(len(cupPositions[0])):
        actionMatrix = stateMatrix.copy()
        actionMatrix[cupPositions[0][i], cupPositions[1][i]] = 0
        currentPower = getRow(stateMatrix, actionMatrix)
        outputIndex += 2 ** currentPower

    return outputIndex


if __name__ == "__main__":

    filePath = "./rawTables/"
    fileNames = os.listdir(filePath)
    # fileNames = ["rawTable_0.00.p"]

    # A dict that will be dumped into a JSON
    outputToJSON = dict()

    for fileName in fileNames:
        print("Working on file: {}".format(fileName))
        fullPath = os.path.join(filePath, fileName)
        with open(fullPath, "rb") as filePointer:
            qTable = pickle.load(filePointer)
        # Log all Q-values in a massive 2D array that will be dumped saved into a dict
        # 65536 = 2^16 to encompass all combinations of 16 cups, 17 is to accomplish a re-rack Q
        currentProcessedQ = np.zeros((65536, 17), dtype=np.int8)
        OriginalQTableKeys = list(qTable.keys())
        # print(OriginalQTableKeys)
        for OriginalQTableKey in qTable.keys():
        # for OriginalQTableKey in OriginalQTableKeys:
            qTableKey = np.array(OriginalQTableKey)
            # print("qTableKey: {}".format(qTableKey))
            # Because of the stupid way I stored the key, it's convoluted to get out the action and state
            stateRecovered = np.vstack((qTableKey[0:7], qTableKey[14:21], qTableKey[28:35], qTableKey[42:49]))
            actionRecovered = np.vstack((qTableKey[7:14], qTableKey[21:28], qTableKey[35:42], qTableKey[49:56]))
            # ignoring reracks for the purpose of the front end
            stateRecovered[0, 0] = 0
            currentQRow = getRow(stateRecovered, actionRecovered)
            currentQColumn = getColumn(stateRecovered)
            currentProcessedQ[currentQColumn, currentQRow] = qTable[OriginalQTableKey]
            
            # print("StateRecovered:\n{}".format(stateRecovered))
            # print("ActionRecovered:\n{}".format(actionRecovered))
            # print("outputRow: {}".format(currentQRow))
            # print("outputColumn: {}".format(currentQColumn))
            # print("outputQ: {}".format(qTable[OriginalQTableKey]))
            

        #Parse out the radius of shooting
        radiusOfShooting = fileName.split("_")[1]
        radiusOfShooting = radiusOfShooting[0:-2]
        # Add a the radiusOfShooting as a key to the dictionary for this table
        # Turn the currentProcessedQ into a list of lists
        outputToJSON[radiusOfShooting] = currentProcessedQ.tolist()
    
    # Output to JSON
    filePath = "./docs/"
    fileName = "processedQTable.json"
    fullPath = os.path.join(filePath, fileName)

    print("Writing data to javascript")
    with open(fullPath, "w") as json_file:
        json.dump(outputToJSON, json_file)

    
        



