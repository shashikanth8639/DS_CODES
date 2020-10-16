class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def createDLL(self,data):
        self.node = Node(data)
        self.head = self.tail = self.node
        self.size += 1
        return
    def insertDLL(self,data,location=None,type="start"):
        if location is None:
            location = self.size
        if self.head is None:
            self.createDLL(data)
        else:
            newNode = Node(data)
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.size += 1
                return
            if location >= self.size:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.size += 1
                return
            if type=="start":
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                newNode.prev = tmpNode
                newNode.next = tmpNode.next
                tmpNode.next.prev = newNode
                tmpNode.next = newNode
                self.size += 1
            else:
                tmpNode = self.tail
                for i in range(location-2):
                    tmpNode = tmpNode.prev
                newNode.next = tmpNode
                newNode.prev = tmpNode.prev
                tmpNode.prev.next = newNode
                tmpNode.prev = newNode
                self.size += 1
                return
    def searchDLL(self,key):
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
    def deleteInDLL(self,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            print("LL is empty!")
            return
        else:
            if self.size == 1:
                self.head = self.tail = None
                return
            if location == 0:
                self.head = self.head.next
                self.head.prev = None
                self.size -= 1
                return
            if location >= self.size:
                self.tail = self.tail.prev
                self.tail.next = None
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
    def deleteDLL(self):
        if self.head is None:
            print("LL is empty!")
            return
        else:
            self.head = self.tail = None
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
    def rev_displayDLL(self):
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