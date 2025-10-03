def powerset(array):
    result = [[]]
    for element in array:
        result += [curr + [element] for curr in result]
    return result
