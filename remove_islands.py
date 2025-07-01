def removeIslands(matrix):
    onesConnectedToBoarder = [[False for _ in matrix[0]] for _ in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix)-1
            colIsBorder = col == 0 or col == len(matrix[row])-1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue

            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBoarder)
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBoarder[row][col]:
                continue
            matrix[row][col] = 0
    return matrix

def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentRow, currentCol = stack.pop()
        if onesConnectedToBorder[currentRow][currentCol]:
            continue
        onesConnectedToBorder[currentRow][currentCol] = True
        neighbours = getNeighbours(matrix, currentRow, currentCol)
        for row, col in neighbours:
            if matrix[row][col] != 1:
                continue
            if onesConnectedToBorder[row][col]:
                continue  # Skip already visited
            stack.append((row, col))

def getNeighbours(matrix, row, col):
    neighbours = []
    numRows = len(matrix)
    numCols = len(matrix[0])

    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if row + 1 < numRows:
        neighbours.append((row + 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < numCols:
        neighbours.append((row, col + 1))

    return neighbours
    