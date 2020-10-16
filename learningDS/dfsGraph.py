class Node:
	def __init__(self,data):
		self.data = data
		self.adjList = []
		self.visited = False
		
class DEPTHFS:
	
	def dfs(self,node):
		node.visited = True
		print(node.data)
		for each in node.adjList:
			if each.visited == False:
				self.dfs(each)
				

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjList.append(node2)
node2.adjList.append(node5)
node3.adjList.append(node3)
node4.adjList.append(node1)

dfs = DEPTHFS()
dfs.dfs(node1)