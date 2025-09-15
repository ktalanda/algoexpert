class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    listOneNodes = set()
    currentNodeOne = linkedListOne
    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)
        currentNodeOne = currentNodeOne.next

    currentNodeTwo = linkedListTwo
    while currentNodeTwo is not None:
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo
        currentNodeTwo = currentNodeTwo.next
    return None


def mergingLinkedLists_2(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    countOne = 0
    while currentNodeOne is not None:
        countOne += 1
        currentNodeOne = currentNodeOne.next
    currentNodeTwo = linkedListTwo
    countTwo = 0
    while currentNodeTwo is not None:
        countTwo += 1
        currentNodeTwo = currentNodeTwo.next

    diff = abs(countTwo - countOne)
    biggerCurrentNode = linkedListOne if countOne > countTwo else linkedListTwo
    smallerCurrentNode = linkedListTwo if countOne > countTwo else linkedListOne

    for _ in range(diff):
        biggerCurrentNode = biggerCurrentNode.next
    
    while biggerCurrentNode is not smallerCurrentNode:
        biggerCurrentNode = biggerCurrentNode.next
        smallerCurrentNode = smallerCurrentNode.next
    
    return biggerCurrentNode


def mergingLinkedLists_3(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListOne
        else:
            currentNodeOne = currentNodeOne.next

        if not currentNodeTwo:
            currentNodeTwo = linkedListTwo
        else:
            currentNodeTwo = currentNodeTwo.next
    return currentNodeOne
