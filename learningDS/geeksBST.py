class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class GFGBsearchTree:
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
    def search(self,key,node=""):
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
            return
        elif key < node.data:
            return self.search(key,node.left)
        else:
            return self.search(key,node.right)
    def insert(self,data,node=""):
        if self.root is None:
            self.root = Node(data)
            return
        # newNode = Node(data)
        if node == "":
            node = self.root
        if node is None:
            node = Node(data)
            return node
        elif  data < node.data:
            node.left = self.insert(data,node.left)
        elif  data >= node.data:
            node.right = self.insert(data,node.right)
        return node
    def delete(self,key,node=""):
        if self.root is None:
            print("TREE IS EMPTY")
            return
        if node == "":
            node = self.root
        if node is None:
            print("IM SORRY! KEY NOT FOUND")
            return
        if key<node.data:
            node.left = self.delete(key,node.left)
        elif key>node.data:
            node.right = self.delete(key,node.right)
        else:
            if node.left is None and node.right is None:
                if node.data == self.root.data:
                    self.root = None
                    return
                node = None
            elif node.left is None:
                if node.data == self.root.data:
                    self.root = self.root.right
                    return
                node = node.right
            elif node.right is None:
                if node.data == self.root.data:
                    self.root = self.root.left
                    return
                node = node.left
            else:
                minNode = self.root.right
                prev = None
                while minNode.left is not None:
                    prev = minNode
                    minNode = minNode.left
                node.data = minNode.data
                if prev is None:
                    self.root.right = None
                else:
                    prev.left = None
        return node



bst = GFGBsearchTree()
bst.insert(2)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(1)
bst.insert(2)
# bst.insert(45)
# bst.insert(12)
# bst.insert(23)
# bst.insert(9)
bst.delete(4)
# bst.insert(36)
# bst.insert(74)
# bst.insert(56)
# bst.insert(68)
# bst.insert(24)
# bst.insert(98)
# bst.delete(45)
# bst.delete(98)
# bst.delete(24)
# bst.delete(68)
# bst.delete(56)
# bst.delete(74)
# bst.delete(36)
# bst.delete(9)
# bst.delete(23)
# bst.delete(12)
# bst.delete(45)
# bst.search(45)
# bst.search(36)
# bst.search(98)
# bst.search(24)
bst.inorder()
print()
bst.levelorder()
print()

