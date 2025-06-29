def riverSizes(matrix):
    sizes = []
    visited = [[False for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i,j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbours(i, j, matrix, visited):
    unvisitedNeighbours = []
    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbours.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbours.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbours.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbours.append([i, j+1])
    return unvisitedNeighbours


def riverSizesRecursive(matrix):
    sizes = []
    visited = [[False for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            currentRiverSize = traverseNodeRecursive(i, j, matrix, visited)
            if currentRiverSize > 0:
                sizes.append(currentRiverSize)
    return sizes

def traverseNodeRecursive(i, j, matrix, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0
    if visited[i][j]:
        return 0
    visited[i][j] = True
    if matrix[i][j] == 0:
        return 0
    
    currentRiverSize = 1
    currentRiverSize += traverseNodeRecursive(i - 1, j, matrix, visited)
    currentRiverSize += traverseNodeRecursive(i + 1, j, matrix, visited)
    currentRiverSize += traverseNodeRecursive(i, j - 1, matrix, visited)
    currentRiverSize += traverseNodeRecursive(i, j + 1, matrix, visited)
    return currentRiverSize