class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    def createCDLL(self,data):
        self.node = Node(data)
        self.node.next = self.node.prev = self.node
        self.head = self.tail = self.node
        self.size += 1
        return
    def insertCDLL(self,data,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            self.createCDLL(data)
            return
        else:
            newNode = Node(data)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
                self.size += 1
                return
            if location >= self.size:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = self.head.prev = newNode
                self.tail = newNode
                self.size += 1
            else:
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                newNode.prev = tmpNode
                newNode.next = tmpNode.next
                tmpNode.next.prev = tmpNode.next = newNode
                self.size += 1
                return
    def searchCDLL(self,key):
        if self.head is None:
            print("LL is empty!")
            return
        else:
            tmpNode = self.head
            for i in range(self.size):
                if tmpNode.data == key:
                    print("KEY FOUND")
                    return
                tmpNode = tmpNode.next
            else:
                print("KEY NOT FOUND")
                return
    def deleteInCDLL(self,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            print("LL is empty!")
            return
        else:
            if self.size == 1:
                self.head.prev = self.head.next = None
                self.head = self.prev = None
                self.size -= 1
                return
            if location == 0:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                self.size -= 1
                return
            if location >= self.size:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
                self.size -= 1
                return
            else:
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                tmpNode.next = tmpNode.next.next
                tmpNode.next.prev = tmpNode
                self.size -= 1
                return
    def deleteCDLL(self):
        if self.head is None:
            print("LL is empty!")
            return
        else:
            self.head.prev = self.head.next = None
            self.head = self.prev = None
            self.size = 0
            return
    def display(self):
        if self.head is None:
            print("LL is empty!")
            return
        else:
            tmpNode = self.head
            for i in range(self.size-1):
                print(tmpNode.data,end="-->")
                tmpNode = tmpNode.next
            print(tmpNode.data)
            return
    def rev_displayCDLL(self):
        if self.head is None:
            print("LL is empty!")
            return
        else:
            tmpNode = self.tail
            for i in range(self.size-1):
                print(tmpNode.data,end="-->")
                tmpNode = tmpNode.prev
            print(tmpNode.data)
            return
