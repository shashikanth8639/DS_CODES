class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class circularsingleLL:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def createCLL(self,data):
        self.node = Node(data)
        self.node.next = self.node
        self.head = self.node
        self.tail = self.node
        self.size += 1
        return
    def insertCLL(self,data,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            self.createCLL(data)
            return
        else:
            newNode = Node(data)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
                self.size += 1
                return
            if location >= self.size:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
                self.size += 1
                return
            else:
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                newNode.next = tmpNode.next
                tmpNode.next = newNode
                self.size += 1
                return
    def searchCLL(self,key):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            tmpNode = self.head
            for i in range(self.size):
                if tmpNode.data == key:
                    print("KEY FOUND")
                    break
                tmpNode = tmpNode.next
            else:
                print("KEY NOT FOUND")
            return
    def deleteInCLL(self,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            if self.size == 1:
                self.head.next = self.tail = self.head = None
                self.size -= 1
                return
            if location == 0:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.size -= 1
                return
            if location >= self.size:
                tmpNode = self.head
                for i in range(self.size-1):
                    tmpNode = tmpNode.next
                tmpNode.next = self.head
                self.tail = tmpNode
                self.size -= 1
                return
            else:
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                tmpNode.next = tmpNode.next.next
                self.size -= 1
    def deleteCLL(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            self.head = self.tail = self.head.next = None
            self.size = 0
            return
    def display(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        tmpNode = self.head
        for i in range(self.size-1):
            print(tmpNode.data,end="-->")
            tmpNode = tmpNode.next
        print(tmpNode.data)
        return
            
    
