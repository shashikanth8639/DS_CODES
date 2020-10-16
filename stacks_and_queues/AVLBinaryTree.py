class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.height = 0
        self.left = None
class AVLTree:
    def __init__(self):
        self.size = 0
        self.root = None
    def createAVL(self,data):
        if self.root is not None:
            print("TREE ALREADY EXISTS")
            return
        self.root = Node(data)
        self.size += 1
    def searchAVL(self,key,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node == "":
            node = self.root
        if node == None:
            print("KEY NOT FOUND")
            return
        if node.data == key:
            print("KEY FOUND")
            return
        elif key < node.data:
            self.searchAVL(key, node.left)
        else:
            self.searchAVL(key, node.right)
    
    def calHeight(self,node):
        if node is None:
            return -1
        else:
            return node.height
    def insertAVL(self,data,curNode=""):
        if self.root is None:
            self.createAVL(data)
            return
        
       
        if curNode == "":
            curNode = self.root
        elif curNode is None:
            self.size += 1
            return Node(data)
        if curNode.data <= curNode.data:
            # print(newNode.data,"IM IN")
            curNode.left = self.insertAVL(data,curNode.left)
            # print(curNode.left.data, "IM GONE")
        else:
            curNode.right = self.insertAVL(data,curNode.right)
        curNode = self.checkBalance(curNode)
        return curNode
    
    def inorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM INORDER")
            node = self.root
        if node.left is not None:
            self.inorderDisplay(node.left)
        print(node.data, node.height)
        if node.right is not None:
            self.inorderDisplay(node.right)
    def preorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM PREORDER")
            node = self.root
        print(node.data)
        if node.left is not None:
            self.inorderDisplay(node.left)
        if node.right is not None:
            self.inorderDisplay(node.right)
    def postorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM POSTORDER")
            node = self.root
        if node.left is not None:
            self.inorderDisplay(node.left)
        if node.right is not None:
            self.inorderDisplay(node.right)
        print(node.data)
    def levelorderDisplay(self):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        print("IM LEVELORDER")
        l = []
        l.append(self.root)
        while l!=[]:
            presentNode = l.pop(0)
            if presentNode.left is not None:
                l.append(presentNode.left)
            if presentNode.right is not None:
                l.append(presentNode.right)
            print(presentNode.data, presentNode.height)
        print(self.size)
    def deleteInAVL(self,key,curNode=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if curNode == "":
                curNode = self.root
            if curNode is None:
                print("KEY NOT FOUND")
                return
            if key < curNode.data:
                print("IM LESS THAN", curNode.data)
                curNode.left = self.deleteInAVL(key,curNode.left)
            elif key > curNode.data:
                print("IM GREATER THAN", curNode.data)
                curNode.right = self.deleteInAVL(key,curNode.right)
            else:
                print("IM EQUALS TO", curNode.data)
                if curNode.left is None and curNode.right is None:
                    print("I DONT HAVE ANY CHILD")
                    if curNode == self.root:
                        self.root = None
                        return
                    curNode = None
                elif curNode.left is None:
                    print("I HAVE RIGHT CHILD",curNode.right.data)
                    if curNode == self.root:
                        self.root = curNode.right
                        return
                    curNode = curNode.right
                elif curNode.right is None:
                    if curNode == self.root:
                        self.root = curNode.left
                        return
                    print("I HAVE LEFT CHILD",curNode.left.data)
                    curNode = curNode.left
                else:
                    print("I HAVE TWO CHILDREN",curNode.left.data,curNode.right.data)
                    minNode = self.successor(curNode.right)
                    curNode.right = self.deleteInAVL(minNode,curNode.right)
                    curNode.data = minNode
        if curNode is not None:        
            curNode = self.checkBalance(curNode)
        if curNode is self.root:
            self.root = curNode
        return curNode

    def successor(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node.left is None:
            print("IM returning")
            print(node.data)
            return node.data
        if node.left is not None:
            print("I HAVE LEFT CHILD",node.left.data)
            return self.successor(node.left)        
    def checkBalance(self,curNode):  
        a = -1 if curNode.left is None else self.calHeight(curNode.left)
        b = -1 if curNode.right is None else self.calHeight(curNode.right)

        curNode.height = max(a, b)+1

        balance = a - b
        print(curNode.data,"A,b--->",a,b)
        if balance > 1:
            a1 = -1 if curNode.left.left is None else self.calHeight(curNode.left.left)
            b1 = -1 if curNode.left.right is None else self.calHeight(curNode.left.right)
            if a1 >= b1:
                # print("IM CR and OWN LORDER")
                if curNode == self.root:
                    self.root = self.rightRotate(curNode)
                else: 
                    curNode = self.rightRotate(curNode)
            else:
                if curNode == self.root:
                    self.root.left = self.leftRotate(self.root.left)
                    self.root = self.rightRotate(self.root)
                else:
                    curNode = self.leftRotate(curNode.left)
                    curNode = self.rightRotate(curNode)
        if balance < -1:
            a1 = -1 if curNode.right.right is None else self.calHeight(curNode.right.right)
            b1 = -1 if curNode.right.left is None else self.calHeight(curNode.right.left)
            if a1 >= b1:
                if curNode == self.root:
                    self.root = self.leftRotate(curNode)
                else: 
                    curNode = self.leftRotate(curNode)
            else:
                if curNode == self.root:
                    print("HEEEEL")
                    self.root.right = self.rightRotate(self.root.right)
                    self.root = self.leftRotate(self.root)
                else:
                    curNode = self.rightRotate(curNode.right)
                    curNode = self.leftRotate(curNode)
        return curNode
    def rightRotate(self,node):
        print("IN LL")
        newNode = node.left
        node.left = newNode.right
        newNode.right = node
        node.height = max(self.calHeight(node.left), self.calHeight(node.right))+1
        newNode.height = max(self.calHeight(newNode.left), self.calHeight(newNode.right))+1
        return newNode
    def leftRotate(self,node):
        print("IN RR")
        newNode = node.right
        node.right = newNode.left
        newNode.left = node
        node.height = max(self.calHeight(node.left), self.calHeight(node.right))+1
        newNode.height = max(self.calHeight(newNode.left), self.calHeight(newNode.right))+1
        return newNode
