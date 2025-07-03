def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue
        containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
        if containsCycle:
            return True
    return False
    
def isNodeInCycle(edges, node, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbours = edges[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            containsCycle = isNodeInCycle(edges, neighbour, visited, currentlyInStack)
            if containsCycle:
                return True
        elif currentlyInStack[neighbour]:
            return True
    currentlyInStack[node] = False
    return False

# ------------------------------------
            
WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph2(edges):
    numberOfNodes = len(edges)
    colours = [WHITE for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if colours[node] != WHITE:
            continue

        containsCycle = traverseAndColourNodes(node, edges, colours)
        if containsCycle:
            return True
    return False

def traverseAndColourNodes(node, edges, colours):
    colours[node] = GREY

    neighbours = edges[node]
    for neighbour in neighbours:
        neighbourColour = colours[neighbour]

        if neighbourColour == GREY:
            return True
        if neighbourColour != WHITE:
            continue

        containsCycle = traverseAndColourNodes(neighbour, edges, colours)
        if containsCycle:
            return True

    colours[node] = BLACK
    return False
