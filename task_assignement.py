def taskAssignment(k, tasks):
    indexedTask = []
    for i in range(len(tasks)):
        indexedTask.append((tasks[i], i))
    indexedTask.sort()
    result = []
    for i in range(k):
        result.append((indexedTask[i][1], indexedTask[-(i + 1)][1]))
    return result
