class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self,data):
        newNode = Node(data)
        if self.front is None:
            newNode = Node(data)
            self.front = self.rear = newNode
            self.size += 1
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.size += 1
    def dequeue(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            if self.size == 1:
                self.front = self.rear = None
                self.size -= 1
            else:
                self.front = self.front.next
                self.size -= 1
    def frontele(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            print(self.front.data)
    def rearele(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            print(self.rear.data)
    def length(self):
        print(self.size)
    def delete(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            self.front = self.rear = None
            self.size = 0
    def display(self):
        if self.front is None:
            print("QUEUE is EMPTY")
        else:
            tmpNode = self.front
            for i in range(self.size):
                print(tmpNode.data)
                tmpNode = tmpNode.next
            

