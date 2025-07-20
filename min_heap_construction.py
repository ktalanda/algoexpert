class MinHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        if not array:
            return []
        lastParentIndex = (len(array) - 2) // 2
        for i in reversed(range(lastParentIndex + 1)):
            self.siftDown(i, len(array) - 1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[indexToSwap] < heap[currentIndex]:
                heap[indexToSwap], heap[currentIndex] = heap[currentIndex], heap[indexToSwap]
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                return
        return

    def siftUp(self, currentIndex, heap):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
            heap[currentIndex], heap[parentIndex] = heap[parentIndex], heap[currentIndex]
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2
        return

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        valueToRemove = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
