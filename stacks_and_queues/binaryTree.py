class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
        self.last = None
        self.size = 0
    def createBT(self,data):
        if self.root is not None:
            print("TREE ALREADY EXISTS")
            return
        else:
            self.root = Node(data)
            self.last = self.root
            self.size += 1
            print("SUCCESSFULLY CREATED")
    def inorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if node is None:
                print("INORDER")
                node = self.root
            if node.left is not None:
                self.inorderDisplay(node.left)
            print(node.data)
            if node.right is not None:
                self.inorderDisplay(node.right)
            
    def preorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if node is None:
                print("PREORDER")
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
        else:
            if node is None:
                print("POSTORDER")
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
        else:
            print("LEVELORDER")
            node = self.root
            l = []
            l.append(node)
            while l != []:
                if l[0].left is not None:
                    l.append(l[0].left)
                if l[0].right is not None:
                    l.append(l[0].right)
                print(l.pop(0).data)
    def searchBT(self,key):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            node = self.root
            l = []
            l.append(node)
            while l != []:
                if l[0].data == key:
                    print("ITEM FOUND")
                    return
                if l[0].left is not None:
                    l.append(l[0].left)
                if l[0].right is not None:
                    l.append(l[0].right)
                l.pop(0)
            else:
                print("NOT FOUND")
    def insertBT(self,data):
        if self.root is None:
            self.root = Node(data)
            self.last = self.root
            self.size += 1
        else:
            newNode = Node(data)
            self.size += 1
            self.last = newNode
            node = self.root
            l = []
            l.append(node)
            while l!= []:
                if l[0].left is None:
                    l[0].left = newNode
                    
                    print("INSERTED SUCCESFULLY")
                    break
                else:
                    l.append(l[0].left)
                if l[0].right is None:
                    l[0].right = newNode
                    print("INSERTED SUCCESFULLY")
                    break
                else:
                    l.append(l[0].right)
                l.pop(0)
    def deleteInBT(self,key=None):
        if self.root is None:
            print("Tree does not ezists")
            return
        else:
            if key is not None:
                l = []
                node = self.root
                l.append(node)
                while l != []:
                    if l[0].left is not None:
                        l.append(l[0].left)
                    if l[0].right is not None:
                        l.append(l[0].right)
                    if l[0].data == key:
                        print("HURRAY")
                        print(self.last.data)
                        l[0].data = self.last.data
                        self.last = None
                        self.size -= 1
                        self.computeLast()
                        print(self.last.data)
                        print("DELTED SUCCESSFULLY")
                        return
                    l.pop(0)
            else:
                self.size -= 1
                self.last = None
                self.computeLast()
                print("DELTED SUCCESSFULLY")
    def computeLast(self):
        l = []
        previousNode = presentNode = None
        node = self.root
        l.append(node)
        while l != []:
            previousNode = presentNode
            presentNode = l.pop(0) 
            if presentNode.left is not None:
                l.append(presentNode.left)
            elif presentNode.left is None:
                previousNode.right = None
            if presentNode.right is not None:
                l.append(presentNode.right)
            elif presentNode.right is None:
                presentNode.left = None
        self.last =previousNode
    def deleteBT(self):
        if self.root is None:
            print("TREE IS EMPTY")
        else: 
            self.root = None
            print("TREE DELETED")

                 

