def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]

    for n in array[1:]:
        maxEndingHere = max(n, maxEndingHere + n)
        maxSoFar = max(maxSoFar, maxEndingHere)
    
    return maxSoFar
