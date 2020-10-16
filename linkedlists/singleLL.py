class Node:
    def __init__(self,nodeValue):
        self.data = nodeValue
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def createLL(self,data):
        self.node = Node(data)
        self.head = self.tail = self.node
        self.size += 1
        print("Node created successfully")
    def insertLL(self,data,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            self.createLL(data)
            return
        else:
            newNode = Node(data)
            
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.size += 1
                print("Node inserted at start successfully")
                return
            if location >= self.size:
                self.tail.next = newNode
                self.tail = newNode
                self.size += 1
                print("Node inserted at last successfully")
                return
            self.tmpNode = self.head
            for i in range(location-2):
                self.tmpNode = self.tmpNode.next
            newNode.next = self.tmpNode.next
            self.tmpNode.next = newNode
            self.size += 1
            print(f"Node inserted at position {location} successfully")
            return
    def searchLL(self,key):
        if self.head is None:
            print("LinkedList is empty!")
            return
        tmpNode = self.head
        for i in range(self.size):
            if tmpNode.data == key:
                print("KEY FOUND")
                return
            tmpNode = tmpNode.next
        print("KEY NOT FOUND")
        return
    def deleteInLL(self,location=None):
        if location is None:
            location = self.size
        if self.head is None:
            print("LinkedList is empty! cannot delete a value")
            return
        else:
            if self.size == 1:
                self.head = self.tail = None
                self.size -= 1
                return
            if location == 0:
                self.head = self.head.next
                self.size -= 1
                print("Node deleted successfully at start")
                return
            if location >= self.size:
                tmpNode = self.head
                for i in range(self.size-2):
                    tmpNode = tmpNode.next
                self.tail = tmpNode
                self.tail.next = None
                self.size -= 1
                print("Node deleted successfully at the end")
                return
            else:
                tmpNode = self.head
                for i in range(location-2):
                    tmpNode = tmpNode.next
                tmpNode.next = tmpNode.next.next
                self.size -= 1
                print(f"Node deleted successfully at position {location}")
                return
    def display(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        tmpNode = self.head
        while tmpNode.next is not None:
            print(tmpNode.data,end="-->")
            tmpNode = tmpNode.next
        print(tmpNode.data)
    def deleteLL(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        self.size  = 0
        self.head = self.tail = None
        
        print("Entire LL is deleted successfully")
        return
    def pairwiseSwap(self):
        temp = self.head
        while temp and temp.next:
            temp.data,temp.next.data = temp.next.data,temp.data
            temp = temp.next.next
    def pairwiseSwapLinks(self):
        temp = self.head
        while temp and temp.next:
            new = temp.next.next
            print(new.data,"IM NEW")
            link1 = temp.next
            # link1.next = None
            print(link1.data,"IM LINK")
            # newtemp = temp
            # newtemp.next = None
            print(temp.data,"INN MEWTEMP")
            link1.next = temp
            link1.next.next = new
            # temp.next = new
            # temp = link1
            # print(temp.data)
            # temp.next = newtemp
            # print(temp.next.data)
            # newtemp.next = new
            # print(newtemp.next.data)
            self.display()
            temp = temp.next.next
            


ll = SingleLinkedList()
ll.insertLL(45)
ll.insertLL(125)
ll.insertLL(89)
ll.insertLL(63)
ll.insertLL(23)
ll.insertLL(19)
ll.insertLL(98)
ll.display()
# ll.pairwiseSwap()
# ll.display()
ll.pairwiseSwapLinks()
ll.display()