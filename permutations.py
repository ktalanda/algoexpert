def getPermutations(array):
    result = helper(array)
    if result == [[]]:
        return []
    return result

def helper(array):
    if len(array) == 0:
        return [[]]

    firstElement = array[0]
    restOfArray = array[1:]

    permutationsOfRest = helper(restOfArray)
    allPermutations = []

    for permutation in permutationsOfRest:
        for i in range(len(permutation) + 1):
            newPermutation = permutation[:i] + [firstElement] + permutation[i:]
            allPermutations.append(newPermutation)

    return allPermutations
