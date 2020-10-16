class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MergeSortForLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insertLL(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
    def sortUsingMergeSort(self):
        # temp = self.head
        # newList = []
        # while temp:
        #     newList.append(temp.data)
        #     temp = temp.next
        
        # newList.sort()
        # temp = self.head
        # i = 0
        # while temp:
        #     temp.data = newList[i]
        #     i += 1
        #     # print(temp.data,'LLl')
        #     temp = temp.next
            
        # self.display()
        if self.head == None or self.tail == None or self.size == 1:
            print("NO NEED OF SORTING")
            return
        print(self.size)
        self.mergeSort(self.head,1,self.size)

    def mergeSort(self,head,start,end):
        if start < end:
            mid = (start+end)//2
            self.mergeSort(head,start,mid)
            self.mergeSort(head,mid+1,end)
            self.merge(head,start,mid,end)
            self.display()
        return

    def merge(self,head,p,q,z):
        l =r = head
        for i in range(p-1):
            l = l.next
        temp = []
        for i in range(q):#-1
            r = r.next
        i,j = p,q
        if p-q == 0:
            i -= 1
            print("I IAM SINGLE")
        if q-z == 0:
            print("JJ IAM SINGLE")
            j -= 1
        while i<q and j<z:
            # t = temp.data
            # print(t)
            if l.data > r.data:
                print(l.data,">",r.data)
                temp.append(r.data)
                # r.data = t
                # l = l.next
                # print(l.data,temp.data)
                # l.data = t
                r = r.next
                j +=1
            else:
                print(l.data,"<",r.data)
                temp.append(l.data)
                # l.data = t
                l = l.next
                i += 1
        print(temp)
        v = self.head
        i = 0
        while i>0 :
            v.data = temp[i]
            v = v.next
        self.display()
        # while i<q :
        #     print("J EMPTY",l.data)
        #     # t = temp.data
        #     temp.data = l.data
        #     # l.data = t
        #     l = l.next
        #     i += 1
        #     temp = temp.next
        # while j<z :
        #     print("I EMPTY")
        #     # t = temp.data
        #     temp.data = r.data
        #     # r.data = t
        #     r = r.next
        #     j += 1
        #     temp = temp.next

    def display(self):
        tempNode = self.head
        while tempNode.next is not None:
            print(tempNode.data,end="-->")
            tempNode = tempNode.next
        print(tempNode.data)


mll = MergeSortForLL()
mll.insertLL(45)
mll.insertLL(128)
mll.insertLL(26)
mll.insertLL(4)
mll.display()
mll.insertLL(19)
mll.insertLL(245)
mll.display()
mll.sortUsingMergeSort()
mll.display()