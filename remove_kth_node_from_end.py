class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head: LinkedList, k: int) -> None:
    first = head
    second = head

    counter = 0
    while counter < k:
        counter += 1
        second = second.next

    if second is None:
        first.value = first.next.value
        first = first.next
        return

    while second.next is not None:
        first = first.next
        second = second.next

    first.next = first.next.next

