
class Heap:
    def __init__(self):
        self.heap = []

    def createHeap(self, elements):
        for i in elements:
            self.insert(i)

    def insert(self, value):
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            parentIndex = (len(self.heap)-2)//2             # (index - 1)/2
            itemIndex = len(self.heap)-1

            while self.heap[parentIndex] < value:
                self.heap[itemIndex] = self.heap[parentIndex]
                self.heap[parentIndex] = value
                itemIndex = parentIndex
                parentIndex = (parentIndex - 1)//2
                if parentIndex < 0:
                    break

    def topElement(self):
        if self.heap:
            return self.heap[0]
        else:
            raise EmptyHeapException()

    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException("The Heap is Empty!")
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        temp = self.heap.pop()

        index = 0
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index  + 2

        while leftChildIndex < len(self.heap):
            if rightChildIndex < len(self.heap) :
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else:
                        break
                    
            else:
                if self.heap[leftChildIndex] > temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break
            
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index  + 2    

        self.heap[index] = temp
        return max_value
                    

    def heapSort(self, list1):
        self.createHeap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0, self.delete())
        except EmptyHeapException:
            pass

        return list2


class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg

    def __str__(self):
        return self.msg


if __name__ == "__main__":
    heap = Heap()
    # heap.createHeap([40, 70 , 10, 90, 60, 30, 50, 20, 80])
    # print(heap.heap)
    # # print(heap.delete())
    # try:
    #     print("Top of the heap", heap.topElement())
    # except Exception as e:
    #     print(e)

    print(heap.heapSort(
        [90, 80, 75, 70, 60, 55, 30, 20, 41, 40, 50, 10, 35, 25]))
    print(heap.heap)
