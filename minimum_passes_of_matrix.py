def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    nextPassQueue = getAllPositivePositions(matrix)
    passes = 0
    while len(nextPassQueue) > 0:
        currentRow, currentCol = nextPassQueue.pop(0)

        adjacentPositions = getAdjacentPosition(currentRow, currentCol, matrix)
        for position in adjacentPositions:
            row, col = position
            value = matrix[row][col]
            if value < 0:
                matrix[row][col] = value * (-1)
                nextPassQueue.append([row, col])
        passes += 1

    return passes

def getAllPositivePositions(matrix):
    positivePositions = []

    for rowId in range(len(matrix)):
        for colId in range(len(matrix[rowId])):
            value = matrix[rowId][colId]
            if value > 0:
                positivePositions.append([rowId, colId])
        return positivePositions

def getAdjacentPosition(row, col, matrix):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row - 1, col])
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])
    if col > 0:
        adjacentPositions.append([row, col - 1])
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions

def containsNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False