class Node:
	
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None
		self.color = 1
		
class REDBLACK:
	
	def __init__(self):
		self.root = None
		self.null = Node(-1)
		self.color = 0
	
	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
			self.root.color = 0
			self.root.left = self.null
			self.root.right = self.null
			return
		newNode = Node(data)
		newNode.left = self.null
		newNode.right = self.null
		self.root = self.insertNode(self.root,newNode)
		self.fixViolation(newNode)
		
	def insertNode(self,node,inode):
		
		if node==self.null:
			return inode
			
		if inode.data < node.data:
			node.left = self.insertNode(node.left,inode)
			node.left.parent = node
		elif inode.data >= node.data:
			node.right = self.insertNode(node.right,inode)
			node.right.parent = node
		
		return node
		
	def fixViolation(self,curNode):
	
		parent = None
		grandParent = None
		
		while curNode!= self.root and  curNode.color == 1 and curNode.parent.color == 1:
			
			parent = curNode.parent
			grandParent = parent.parent
			
			if parent == grandParent.left:
				
				uncle = grandParent.right
				
				if uncle is not None and uncle.color == 1:
				
					grandParent.color = 1
					parent.color = 0
					uncle.color = 0
					curNode = grandParent
				
				else:
					
					if curNode == parent.right:

						self.leftRotate(parent)
						curNode = parent
						parent = curNode.parent

					self.rightRotate(grandParent)
					parent.color,grandParent.color = grandParent.color,parent.color
					curNode = parent
			else:
				
				uncle = grandParent.left
				
				if uncle is not None and uncle.color == 1:
					
					grandParent.color = 1
					parent.color = 0
					uncle.color = 0
					curNode = grandParent
					
				else:
					
					if curNode == parent.left:
						
						self.rightRotate(parent)
						curNode = parent
						parent = curNode.parent
					
					self.leftRotate(grandParent)
					parent.color,grandParent.color = grandParent.color,parent.color
					curNode = parent
					
		self.root.color = 0
		
	def rightRotate(self,node):
		#tmp = node.parent
		
		newNode = node.left
		node.left = node.left.right
		if node.left is not None:
			node.left.parent = node
		newNode.parent = node.parent
		if node.parent is None:
			self.root = newNode
		elif node == node.parent.left:
			node.parent.left = newNode
		else:
			node.parent.right = newNode
		newNode.right = node
		node.parent = newNode
		
	def leftRotate(self,node):
		
		newNode = node.right
		
		node.right = newNode.left
		if node.right is not None:
			node.right.parent = node
			
		newNode.parent = node.parent
		if node.parent is None:
			self.root = newNode
		elif node == node.parent.right:
			node.parent.right = newNode
		else:
			node.parent.left = newNode
		
		newNode.left = node
		node.parent = newNode
		
		
	def levelorderDisplay(self):
            print("IM IN LEVELORDER")
            q = []
            q.append(self.root)
            while q!=[]:
                curNode = q.pop(0)
                if curNode.left is not self.null:
                    q.append(curNode.left)
                if curNode.right is not self.null:
                    q.append(curNode.right)
                print(curNode.data,end=" ")
	def ino(self):
		self.inorder(self.root)
	def inorder(self,root):
		if root:
			self.inorder(root.left)
			print(root.data,end=" ")
			self.inorder(root.right)

# rb = REDBLACK()
# # rb.insert(7); 
# # rb.insert(6); 
# # rb.insert(5); 
# # rb.insert(4); 
# # rb.insert(3); 
# # rb.insert(2); 
# # rb.insert(1);
# rb.insert(7)
# rb.insert(3)
# rb.insert(11)
# rb.insert(10)
# rb.insert(22)
# rb.insert(8)
# rb.insert(11)
# rb.insert(26)
# rb.insert(2)
# rb.insert(6)
# rb.insert(13)
# rb.levelorder()
# print()
# rb.ino()
tree = REDBLACK()
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