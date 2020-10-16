# class BTNode:
	# def __init__(self,t,isLeaf):
		# self.t = t
		# self.isLeaf = isLeaf
		# self.keys = [0]*(2*t-1)
		# self.child = [None]*(2*t)
		# nKeys = 0

class BTreeNode:
	def __init__(self, isLeaf=False):
		self.isLeaf = isLeaf
		self.keys = []
		self.child = []

class BTree:
	def __init__(self, t):
		self.root = BTNode(True)
		self.t = t
	
	def printTree(self, node, level=0):
		print("LEVEL: ",level," ",len(node.keys), end=":")
		for each in node.keys:
			print(each, end=" ")
		print()
		level += 1
		if node.child !=[]:
			for each in node.child:
				self.printTree(node.child, level)
	
	def search(self, key, node=None):
		if node is None:
			return self.search(key, self.root)
		i = 0
		while i<len(node.keys) and k> node.keys[i]:
			i+=1
		
		if i<len(node.keys) and k==node.keys[i]:
			return (node,i)
		elif node.isLeaf:
			return None
		else:
			return self.search(key, node.child[i])
	
	def insert(self, key):
		root = self.root
		if len(root.keys) == (2*self.t-1):
			tmp = BTNode()
			self.root = tmp
			tmp.child.insert(0, root)
			self.splitChild(tmp, 0)
			self.insertNonFull(tmp, k)
		else:
			self.insertNonFull(root, k)
	
	def insertNonFull(self, node, key):
		i = len(node.keys)-1
		if node.isLeaf:
			node.keys.append((None, None))
			
			
	
class Btree:
	def __init__(self, t):
		self.root=None
		self.t = t
	
	def traverse(self, node, n):
		for i in range(n):
			if not node.isLeaf and node.child[i] is not None:
				self.traverse(node.child[i], node.child[i].nKeys)
			print(node.keys[i],end=" ")
		if not node.isLeaf and node.child[i] is not None:
			self.traverse(node.child[i], node.child[i].nkeys)
	
	def serach(self,node ,key):
		i=0
		while i< node.nKeys and key > node.keys[i]:
			i+=1
		if node.keys[i]==key:
			return node
		if isLeaf:
			return None
		return self.search(node.child[i], key)
	
	
	def insert(self, key):
		if self.root is None:
			self.root = BTNode(True)
			self.root.keys[0] = key
			return
		if self.root.nKeys == 2*t-1 :
			newBtreeNode = BTNode(t, False)
			newBtreeNode.child[0] = self.root
		
		else:
			
			
	
	def splitChild(self, i, btreeNode):
		newBtreeNode = BTNode(btreeNode.t, btreeNode.isLeaf)
		newBtreeNode.nKeys = t-1
		
		for j in range(0,t-1):
			newBtreeNode.keys[j] = btreeNode.keys[j+t]
		
		if not btreeNode.isLeaf:
			for j in range(0,t):
				newBtreeNode.child[j] = btreeNode.child[t+j]
		btreeNode.nKeys = t-1
		for j in range(btreeNode.nKeys, i, -1):
			btreeNode.child[j+1] = btreeNode.child[j]
		btreeNode.child[i+1] = newBtreeNode	
		
		