class binaryHeap:

    def __init__(self):
        self.arr = []
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            print("HEAP IS EMPTY")
            return True

    def peek(self):
        if self.isEmpty():
            return
        return self.arr[0]

    def insert(self,data):
        arr.append(data)
        self.size += 1
        self.heapify(self.size)

    def heapify(self,size):
        
        if self.isEmpty():
            return
        