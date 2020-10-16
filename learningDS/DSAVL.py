class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 0
		
class AVLTree:
	
	def __init__(self):
		self.root = None
		
	def callHeight(self,node):
		if node is None:
			return -1
		
		return node.height
		
	def insert(self,data):
		
		self.root = self.insertNode(self.root,data)
		
	def insertNode(self,node,data):
		
		if node is None:
			return Node(data)
		
		if data < node.data:
			node.left = self.insertNode(node.left,data)
		
		elif data >= node.data:
			node.right = self.insertNode(node.right,data)
			
		node.height = max(self.callHeight(node.left), self.callHeight(node.right)) + 1
		
		node = self.checkBalance(node)
		
		return node
		
	def delete(self,data):
		
		self.root = self.deleteNode(self.root,data)
		
	def deleteNode(self,node,data):
	
		if node is None:
			print("KEY TO BE DELETED IS NOT FOUND")
			return
			
		if data < node.data:
			node.left = self.deleteNode(node.left,data)
		
		elif data > node.data:
			node.right = self.deleteNode(node.right,data)
		
		else:
			if node.left is None and node.right is None:
				return None
				
			if node.left is None:
				node = node.right
				
			elif node.right is None:
				node = node.left
				
			else:
				successor = node.right
				while successor.left is not None:
					successor = successor.left
					
				node.data = successor.data
				node.right = self.deleteNode(node.right,successor.data)
				
			
		node.height = max( self.callHeight(node.left), self.callHeight(node.right) ) + 1
		
		node = self.checkBalance(node)
		
		return node
		
	def checkBalance(self,node):
		
		left_height = self.callHeight(node.left)
		right_height = self.callHeight(node.right)
		
		balance = left_height - right_height
		
		if balance > 1:
			
			left_left_height = self.callHeight(node.left.left)
			left_right_height = self.callHeight(node.left.right)
			
			if left_left_height >= left_right_height:
				return self.rightRotate(node)
				
			else:
				node.left = self.leftRotate(node.left)
				return self.rightRotate(node)
		if balance < -1:
			
			right_right_height = self.callHeight(node.right.right)
			right_left_height = self.callHeight(node.right.left)
			
			if right_right_height >= right_left_height:
				return self.leftRotate(node)
				
			else:
				node.right = self.rightRotate(node.right)
				return self.leftRotate(node)
				
		return node
	
	def rightRotate(self,node):
		
		newNode = node.left
		node.left = node.left.right
		newNode.right = node
		
		node.height = max( self.callHeight(node.left), self.callHeight(node.right) ) + 1
		
		newNode.height = max( self.callHeight(newNode.left), self.callHeight(newNode.right) ) + 1
		
		return newNode
		
	def leftRotate(self,node):
	
		newNode = node.right
		node.right = node.right.left
		newNode.left = node
		
		node.height = max( self.callHeight(node.left), self.callHeight(node.right) ) + 1
		
		newNode.height = max( self.callHeight(newNode.left), self.callHeight(newNode.right) ) + 1
		
		return newNode
		
	def levelorder(self):
		if self.root is not None:
			self.levelorderTraversal(self.root)
	
	def levelorderTraversal(self,root):
		q = []
		q.append(root)
		while q!=[]:
			presentNode = q.pop(0)
			if presentNode.left is not None:
				q.append(presentNode.left)
			if presentNode.right is not None:
				q.append(presentNode.right)
			print(presentNode.data,end=" ")
		
avl = AVLTree()

avl.insert(45)
avl.insert(23)
avl.insert(36)
avl.insert(56)
avl.insert(49)
avl.insert(29)
avl.delete(56)
avl.delete(45)
avl.delete(49)
avl.delete(23)
avl.delete(29)
avl.delete(36)
# avl.inorder()
avl.levelorder()
		