class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data,pos=None):
        newNode = Node(data)
        if self.head is None:
            self.tail=self.head=newNode
            self.tail.next=self.head
        elif pos==None:
            newNode.next=self.tail.next
            self.tail.next=newNode
            self.tail=newNode
        else:
            self.insertNode(newNode,pos)
    def insertNode(self,newNode,pos):
        if pos==0:
            newNode.next=self.head
            self.tail.next=newNode
            self.head=newNode
        else:
            tmp=self.head
            i=1
            print(self.head.data,i,pos)
            while tmp.next!=self.head and i<pos-1:
                # print(tmp.next.data,i)
                tmp=tmp.next
                i+=1
            newNode.next=tmp.next
            tmp.next=newNode
            if tmp==self.tail:
                self.tail=newNode
    
    def serach(self,data):
        if self.head is None:
            print('CLL IS EMPTY')
            return
        tmp=self.head
        while tmp.next!=self.head:
            if tmp.data==data:
                print("DATA FOUND")
                return
            tmp=tmp.next
        else:
            if tmp.data==data:
                print("DATA FOUND")
            else:
                print("NOT FOUND")
        return
    def delete(self,pos=None):
        if self.head is None:
            print("CLL EMPTY")
            return
        if self.head==self.head.next:
            self.tail=self.head=None
            return
        if pos==None:
            pos=45
        print(self.head.data,self.tail.data)
        tmp=self.head
        i=1
        while tmp.next!=self.tail and i<pos-1:
            # print(tmp.data)
            tmp=tmp.next
            i+=1
        if tmp.next == self.tail:
            tmp.next=self.head
            self.tail=tmp
        elif tmp==self.head:
            self.tail.next=self.head.next
            self.head=self.tail.next
        else:
            tmp.next=tmp.next.next
    def display(self):
        if self.head is None:
            print("CLL EMPTY")
            return
        tmp=self.head
        while tmp.next!=self.head:
            print(tmp.data,end="-->")
            tmp=tmp.next
        print(tmp.data)

CLL= CircularLL()
CLL.insert(45)
CLL.display()
CLL.insert(23)
CLL.display()
CLL.insert(198)
CLL.display()
CLL.insert(2)
CLL.display()
CLL.insert(598,0)
CLL.display()
CLL.insert(597,45)
CLL.display()
CLL.insert(162,4)
CLL.display()
CLL.serach(198)
CLL.display()
CLL.serach(597)
CLL.display()
CLL.serach(145)
CLL.display()
CLL.delete()
CLL.display()
CLL.delete(0)
CLL.display()
CLL.delete(98)
CLL.display()
CLL.delete(3)
CLL.display()
CLL.delete()
CLL.display()
CLL.delete()
CLL.display()
CLL.delete()
CLL.display()
CLL.delete()
CLL.display()
         