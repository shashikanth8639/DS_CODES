class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1
class RedBlackTree:
    def __init__(self):
        self.null = Node(-1)
        self.null.color = 0
        self.root = None
        # self.root = self.null
    def delete(self,data):
        if not self.root:
            print("TREE is empty")
            return

        self.deleteRBT(self.root,data)
    def deleteRBT(self,curNode,data):
        if curNode==self.null:
            print("Data to be deleted not found.")
            return
        if data<curNode.data:
            self.deleteRBT(curNode.left, data)
        elif data>curNode.data:
            self.deleteRBT(curNode.right, data)
        else:
            if curNode.left==curNode.right==self.null:
                print("HEY1")
                doubleBlack=False
                if curNode.color==0:
                    print("HEY")
                    doubleBlack=True
                if curNode==self.root:
                    self.root=self.null
                    curNode=self.root
                elif curNode==curNode.parent.left:
                    curNode.parent.left=self.null
                    curNode.parent.left.parent=curNode.parent
                    curNode=curNode.parent.left
                else:
                    curNode.parent.right=self.null
                    curNode.parent.right.parent=curNode.parent
                    curNode=curNode.parent.right
                if doubleBlack:
                    self.fixDoubleBlack(curNode)
            elif curNode.left==self.null:
                print("HEY2")
                doubleBlack=False
                if curNode.color==curNode.right.color:
                    doubleBlack=True
                # if curNode.parent is not None:
                curNode.right.parent=curNode.parent
                if curNode==self.root:
                    self.root=curNode.right
                    # self.root.parent=None
                    curNode=self.root
                elif curNode==curNode.parent.left:
                    curNode.parent.left=curNode.right
                    # curNode.right.parent=curNode.parent
                    curNode=curNode.parent.left
                else:
                    curNode.parent.right=curNode.right
                    # curNode.right.parent=curNode.parent
                    curNode=curNode.parent.right
                curNode.color=0
                if doubleBlack:
                    self.fixDoubleBlack(curNode)
            elif curNode.right==self.null:
                print("HEY3")
                doubleBlack=False
                if curNode.color==curNode.left.color:
                    doubleBlack=True
                # if curNode.parent is not None:
                curNode.right.parent=curNode.parent
                if curNode==self.root:
                    self.root=curNode.left
                    # self.root.parent=None
                    curNode=self.root
                elif curNode==curNode.parent.left:
                    curNode.parent.left=curNode.left
                    # curNode.left.parent=curNode.parent
                    curNode=curNode.parent.left
                else:
                    curNode.parent.right=curNode.left
                    # curNode.left.parent=curNode.parent
                    curNode=curNode.parent.left
                curNode.color=0
                if doubleBlack:
                    self.fixDoubleBlack(curNode)
            else:
                print("HEY4")
                tmp=curNode.right
                while tmp.left!=self.null:
                    tmp=tmp.left
                curNode.data=tmp.data
                print(tmp.data)
                self.deleteRBT(curNode.right,tmp.data)
            self.root.color=0
                    
    def fixDoubleBlack(self, curNode):
        sibling = None
        parent = None
        if curNode==self.root:
            return
        parent=curNode.parent
        if parent!=None:
            print("parent sibs")
            if curNode==parent.right:
                sibling=parent.left
            else:
                sibling=parent.right
            #If sibling is black...
        if sibling==self.null:
            print("Sibling is null")
            self.fixDoubleBlack(parent)
        if sibling.color==0:
            print("Sibling color is black")
            #If one of the sibling colors is red...
            if sibling.left.color==1 or sibling.right.color==1:
                #Left-Left color...
                print("One of the child is red")
                if parent.left==sibling:
                    if sibling.left.color==1:
                        print("LL case")
                        sibling.left.color=sibling.color
                        sibling.color=parent.color
                        self.rightRotate(parent)
                        print(parent.data)
                        print(parent.parent.data,"jjj")
                    else:
                        print("LR case")
                        sibling.right.color=parent.color
                        self.leftRotate(sibling)
                        self.rightRotate(parent)
                else:
                    if sibling.right.color==1:
                        print("RR case")
                        sibling.right.color=sibling.color
                        sibling.color=parent.color
                        self.leftRotate(parent)
                    else:
                        print("RL case")
                        sibling.left.color=parent.color
                        self.rightRotate(sibling)
                        self.leftRotate(parent)
                parent.color=0
            elif sibling.left.color==0 and sibling.right.color==0:
                print("Both of the sibling child are black")
                sibling.color=1
                if parent.color==1:
                    parent.color=0
                else:
                    self.fixDoubleBlack(parent)
        else:
            print("Sibling color is red")
            parent.color=1
            sibling.color=0
            if parent.left==sibling:
                self.rightRotate(parent)
            else:
                self.leftRotate(parent)
            self.fixDoubleBlack(curNode)

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            self.root.color = 0
            self.root.left = self.null
            self.root.right = self.null
            return
        self.insertRBT(data)

    def insertRBT(self,data):
        
        newNode = Node(data)
        newNode.left = self.null
        newNode.right = self.null
        tmpNode = None
        curNode = self.root

        while curNode != self.null:
            tmpNode = curNode
            if newNode.data < curNode.data:
                curNode = curNode.left
            else:
                curNode = curNode.right
        newNode.parent = tmpNode
        if newNode.data < tmpNode.data:
            tmpNode.left = newNode
        else:
            tmpNode.right = newNode
        if newNode.parent is None:
            return
        if newNode.parent.parent == None:
            return
        self.checkVioaltion(newNode)
    def checkVioaltion(self,curNode):
        print(curNode.data,"IM IN VIOLATION")
        while curNode!=self.root and curNode.parent.color == 1:
            parent = curNode.parent
            grandparent = curNode.parent.parent
            if parent == grandparent.left:
                if grandparent.right is not self.null:
                    uncle = grandparent.right
                    if uncle.color == 1:
                        print("I HAVE AN UNCLE",uncle.data,"WHOOSE COLOR IS RED")
                        parent.color = uncle.color = 0
                        grandparent.color = 1
                        curNode = grandparent
                    else:
                        if curNode == curNode.parent.left:
                            print("IM ROTATING RIGHT")
                            parent.color = 0
                            grandparent.color = 1
                            self.rightRotate(grandparent)
                        else:
                            print("IM ROTATING LEFT AND RIGHT")
                            self.leftRotate(curNode.parent)
                            # parent.color = 0
                            curNode.color=0
                            grandparent.color = 1
                            self.rightRotate(grandparent)
            else: #curnode.parent == curNode.parent.parent.right
                if grandparent.left is not self.null:
                    uncle = grandparent.left
                    if grandparent.left.color == 1:
                        print("I HAVE AN UNCLE",uncle.data,"WHOOSE COLOR IS RED")
                        parent.color = uncle.color = 0
                        grandparent.color = 1
                        curNode = grandparent
                    else:
                        if curNode == parent.right:
                            print("IM ROTATING LEFT")
                            parent.color = 0
                            grandparent.color = 1
                            self.leftRotate(grandparent)
                        else:
                            print("IM ROTATING RIGHT AND LEFT")
                            self.rightRotate(curNode.parent)
                            grandparent.color = 1
                            curNode.color=0
                            self.leftRotate(grandparent)
        self.root.color = 0
        print("IM OUT OF VIOLATION", curNode.data, curNode.color)
    def inorderDisplay(self,node=None):
        if self.root is None or self.root==self.null:
            print("TREE IS EMPTY")
            return
        if node is None:
            print("IM INORDER")
            node = self.root
        # if node.left is not None:
        if node.left!=self.null:
            self.inorderDisplay(node.left)
        print(node.data,end=" ")
        if node.right != self.null:
            self.inorderDisplay(node.right)
    def levelorderDisplay(self):
        if self.root is None or self.root==self.null:
            print("TREE IS EMPTY")
            return
        print("IM LEVELORDER")
        l = []
        l.append(self.root)
        print("STARTED")
        while l!=[]:
            presentNode = l.pop(0)
            if presentNode.left !=self.null:
                l.append(presentNode.left)
            if presentNode.right!=self.null:
                l.append(presentNode.right)
            print(presentNode.data,"-->",presentNode.color,end=" ")
    def searchRBT(self,key):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        l = []
        l.append(self.root)
        while l!=[]:
            presentNode = l.pop(0)
            if presentNode.data == key:
                print("KEY FOUND")
                return
            if presentNode.left is not None:
                l.append(presentNode.left)
            if presentNode.right is not None:
                l.append(presentNode.right)
        print("KEY NOT FOUND")
        return
    def rightRotate(self,curNode):
        newNode = curNode.left
        curNode.left = newNode.right
        if curNode.left is not self.null:
            curNode.left.parent = curNode
        newNode.parent = curNode.parent
        if curNode.parent is None:
            self.root = newNode
        elif curNode == curNode.parent.right:
            curNode.parent.right = newNode
        else:
            curNode.parent.left = newNode            
        newNode.right = curNode
        curNode.parent = newNode
        # self.root = newNode
        return newNode
    def leftRotate(self,curNode):                                                     
        newNode = curNode.right
        curNode.right = newNode.left
        if curNode.right is not self.null:
            curNode.right.parent = curNode
        newNode.parent = curNode.parent
        if curNode.parent is None:
            self.root = newNode
        elif curNode == curNode.parent.left:
            curNode.parent.left = newNode
        else:
            curNode.parent.right = newNode
        newNode.left = curNode
        curNode.parent = newNode
        return newNode
    
# rbt=RedBlackTree()
# rbt.insert(45)
# rbt.insert(32)
# rbt.insert(21)
# rbt.insert(66)
# rbt.inorderDisplay()
# print()
# rbt.levelorderDisplay()
# print()
# rbt.delete(66)

# rbt.inorderDisplay()
# print()
# rbt.levelorderDisplay()
tree = RedBlackTree()
tree.insert(7)
tree.levelorderDisplay()
print()
tree.insert(3)
tree.levelorderDisplay()
print()
tree.insert(18)
tree.levelorderDisplay()
print()
tree.insert(10)
tree.levelorderDisplay()
print()
tree.insert(22)
tree.levelorderDisplay()
print()
tree.insert(8)
tree.levelorderDisplay()
print()
tree.insert(11)
tree.levelorderDisplay()
print()
tree.insert(26)
tree.levelorderDisplay()
print()
tree.insert(2)
tree.levelorderDisplay()
print()
tree.insert(6)
tree.levelorderDisplay()
print()
tree.insert(13)
tree.levelorderDisplay()
print()
tree.insert(1)
tree.levelorderDisplay()
print("DDDDDDDDDDDDDDDDDDD") 
tree.delete(18)
tree.levelorderDisplay()
print()
tree.delete(11)
tree.levelorderDisplay()
print()
tree.delete(3)
tree.levelorderDisplay()
print()
tree.delete(10)
tree.levelorderDisplay()
print()
tree.delete(22)
tree.levelorderDisplay()
print()
tree.delete(8)
tree.levelorderDisplay()
print()
tree.delete(6)
tree.levelorderDisplay()
print()
tree.delete(7)
tree.levelorderDisplay()
print()
tree.delete(26)
tree.levelorderDisplay()
print()
tree.delete(13)
tree.levelorderDisplay()
print()
tree.delete(2)
tree.levelorderDisplay()
print()
tree.delete(1)
tree.levelorderDisplay()
print()