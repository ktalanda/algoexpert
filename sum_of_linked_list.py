class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedList(listOne, listTwo):
    head = LinkedList(0)
    current = head
    carry = 0

    while listOne is not None or listTwo is not None or carry != 0:
        valueOne = listOne.value if listOne is not None else 0
        valueTwo = listTwo.value if listTwo is not None else 0
        sum = valueOne + valueTwo + carry
        current.next = LinkedList(sum % 10)
        current = current.next
        carry = sum // 10

        listOne = listOne.next if listOne is not None else None
        listTwo = listTwo.next if listTwo is not None else None

    return head.next
