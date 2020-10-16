class Heap:
    def __init__(self):
        self.heap=[]
    def heapify(self,n,parent):
        left = parent*2+1
        right = parent*2+2
        largest=parent
        if left<n and self.heap[parent]<self.heap[left]:
            largest = left
        if right<n and self.heap[largest]<self.heap[right]:
            largest = right
        
        if largest!=parent:
            self.heap[parent],self.heap[largest] = self.heap[largest],self.heap[parent]
            self.heapify(n,largest)
            
    def heapifyBottomToTop(self,i):
        while i!=0 and i//2>=0:
            if self.heap[i//2]>self.heap[i]:
                self.heap[i//2],self.heap[i]=self.heap[i],self.heap[i//2]
            i//=2
    
    def heapifyTopToBottom(self,i):
        size = len(self.heap)
        while(i*2+1<=size-1):
            maxChild = self.maxc(i)
            if self.heap[maxChild]<self.heap[i]:
                self.heap[maxChild],self.heap[i] = self.heap[i],self.heap[maxChild]
            i = maxChild
    
    def maxc(self,i):
        if i*2+2>len(self.heap)-1:
            return i*2+1
        else:
            if self.heap[i*2+1]<self.heap[i*2+2]:
                return i*2+1
            else:
                return i*2+2

    def insert(self,data):
        self.heap.append(data)
        size = len(self.heap)
        # if size!=1:
        self.heapifyBottomToTop(size-1)
        # if size!=1:
        #     for i in range(size//2-1,-1,-1):
        #         self.heapify(size, i)
    
    def extract(self):
        # for i in range(size):
        #     if data == self.heap[i]:
        #         break
        print(self.heap[0],end=" ")
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        self.heap.pop()
        # size = len(self.heap)
        self.heapifyTopToBottom(0)
        # for i in range(size//2-1,-1,-1):
        #     self.heapify(size,i)
        
    
    def display(self):
        for each in self.heap:
            print(each,end=' ')
        print()


n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

heap = Heap()
for each in arr:
    heap.insert(each)
heap.display()
for i in range(n):
    heap.extract()