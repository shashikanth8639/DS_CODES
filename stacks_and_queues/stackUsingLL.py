class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def push(self,data):
        if self.head is None:
            self.node = Node(data)
            self.head = self.tail = self.node
            self.size += 1
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            self.size += 1
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        else:
            if self.size == 1:
                self.head = self.tail = None
                self.size -= 1
            else:
                tmpNode = self.head
                self.head = self.head.next
                self.size -= 1
                return tmpNode.data
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return
        else:
            return self.head.data
    def delete(self):
        if self.head is None:
            print("Stack is empty")
            return
        else:
            self.head = self.tail = None
            return
    def length(self):
        return self.size
    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        else:
            tmpNode = self.head
            for i in range(self.size):
                print(tmpNode.data)
                tmpNode = tmpNode.next
