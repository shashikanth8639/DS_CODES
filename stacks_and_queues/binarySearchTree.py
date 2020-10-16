class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
    def createBST(self,data):
        if self.root is not None:
            print("TREE ALREADY EXISTS")
            return
        self.root = Node(data)
        self.size += 1
        print("IM CREATED")
    def searchBST(self,key,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node == "":
            node = self.root
        if node is None:
            print("KEY NOT FOUND")
            return
        if node.data == key:
            print("KEY FOUND")
        elif node.data > key:
            self.searchBST(key, node.left)
        else:
            self.searchBST(key, node.right)
    def inorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM INORDER")
            node = self.root
        stack = []
        while stack!=[] or node != None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.data,end="->")
            node = node.right
    def inorderDisplayR(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM INORDER")
            node = self.root
        if node.left is not None:
            self.inorderDisplay(node.left)
        print(node.data,end="->")
        if node.right is not None:
            self.inorderDisplay(node.right)
            
        

    def preorderDisplay(self,node=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM PREORDER")
            node = self.root
        print(node.data,end="->")
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
        print(node.data,end="->")
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
            print(presentNode.data,end="->")
    def insertBST(self,data,curNode=""):
        if self.root is None:
            self.createBST(data)
            return
        newNode = Node(data)
        if curNode == "":
            print("IM AT START")
            curNode = self.root
        if curNode is None:
            print("HIP_HPO")
            curNode = newNode
            self.size += 1
            print(self.root.data)
        elif newNode.data <= curNode.data:
            print("IM LESS THAN MY PARENT")
            curNode.left = self.insertBST(data,curNode.left)
        elif newNode.data > curNode.data:
            print("IM LESS THAN MY PARENT")
            curNode.right = self.insertBST(data,curNode.right)
        return curNode
    def delteINBST(self,key,curNode=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            print("IM IN DELETION",key)
            if curNode == "":
                curNode = self.root
            if key < curNode.data and curNode.left is not None:
                curNode.left = self.delteINBST(key,curNode.left)
            elif key > curNode.data  and curNode.right is not None:
                curNode.right = self.delteINBST(key,curNode.right)
            elif key == curNode.data:
                print("YES KEY IS CURNODE")
                self.size -= 1
                if curNode.left is None and curNode.right is None:
                    if curNode == self.root:
                        self.root = None
                    else:
                        curNode = None
                elif curNode.left is None:
                    if curNode == self.root:
                        self.root = self.root.right
                        self.root.right = None
                    else:
                        curNode = curNode.right
                elif curNode.right is None:
                    if curNode == self.root:
                        self.root = self.root.left
                        self.root.left = None
                    else:
                        curNode = curNode.left
                else:
                    node = self.root.right
                    prev = None
                    while node.left is not None:
                        prev = node
                        node = node.left
                    curNode.data = node.data
                    if prev is None:
                        self.root.right = None
                    else:
                        prev.left = None
            else:
                print("KEY NOT FOUND")
        return curNode
    def deletBST(self):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            self.root = None

            
        
