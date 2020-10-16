class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class GFGbinaryTree:
    def __init__(self):
        self.root = None
    def inorder(self,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if node == "":
                node = self.root
            if node.left is not None:
                self.inorder(node.left)
            print(node.data,end=" ")
            if node.right is not None:
                self.inorder(node.right)
    def preorder(self,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if node == "":
                node = self.root
            print(node.data,end=" ")
            if node.left is not None:
                self.inorder(node.left)
            if node.right is not None:
                self.inorder(node.right)
    def postorder(self,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            if node == "":
                node = self.root
            if node.left is not None:
                self.inorder(node.left)
            if node.right is not None:
                self.inorder(node.right)
            print(node.data,end=" ")
    def levelorder(self,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            q = []
            q.append(self.root)
            while q!=[]:
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                print(node.data,end=" ")
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        newNode = Node(data)
        q = []
        q.append(self.root)
        while q!=[]:
            node = q.pop(0)
            if node.left is None:
                node.left = newNode
                return
            q.append(node.left)
            if node.right is None:
                node.right = newNode
                return
            q.append(node.right)
    def computeLast(self):
        prev = cur = None
        tmp = None
        if self.root.left is None and self.root.right is None:
            self.root = None
            return None
        q = []
        q.append(self.root)
        while q!= []:
            prev = cur
            cur = q.pop(0)
            if cur.left is not None:
                q.append(cur.left)
            elif cur.left is None:
                tmp = prev.right.data
                prev.right = None
                return tmp
            if cur.right is not None:
                q.append(cur.right)
            elif cur.right is None:
                tmp = cur.left.data
                cur.left = None
                return tmp
        return tmp
    def delete(self,data=None):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if data is None:
            self.computeLast()
            return
        else:
            q = []
            prev = None
            q.append(self.root)
            while q!=[]:
                node = q.pop(0)
                if node.data == data:
                    node.data = self.computeLast()
                    return
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            else:
                print("KEY NOT FOUND")
                return
    def deleteBT(self):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        else:
            self.root = None
            return
    

        
        
bt = GFGbinaryTree()
bt.insert(45)
bt.insert(12)
bt.insert(23)
bt.insert(9)
bt.insert(36)
bt.insert(74)
bt.insert(56)
bt.insert(68)
bt.insert(24)
bt.insert(98)
# bt.delete()
# bt.delete(98)
# bt.delete(24)
# bt.delete(68)
bt.delete(56)
# bt.delete(74)
# bt.delete(36)
# bt.delete(9)
# bt.delete(23)
# bt.delete(12)
bt.delete(45)
bt.inorder()
print()
bt.levelorder()
print()

    