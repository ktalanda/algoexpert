def hasSingleCycle(array: list[int]):
    visitedCount = 0
    currentId = 0

    while visitedCount < len(array):
        if visitedCount > 0 and currentId == 0:
            return False
        visitedCount+=1
        currentId = next(currentId, array)
    return currentId == 0

def next(currentId: int, array: list[int]):
    jump = array[currentId]
    nextId = (currentId + jump) % len(array)
    return nextId if nextId > 0 else nextId + len(array)
