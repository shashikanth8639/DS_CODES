class Node:
	def __init__(self,data):
		self.data = data
		self.adjList = []
		self.visited = False
		
class BreadthFS:
	
	def bfs(self,node):
		q = []
		q.append(node)
		node.visited = True
		while q!=[]:
			node = q.pop(0)
			
			for each in node.adjList:
				if each.visited == False:
					q.append(each)
					each.visited = True
			print(node.data)
			
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjList.append(node2)
node2.adjList.append(node5)
node3.adjList.append(node3)
node4.adjList.append(node1)

bfs = BreadthFS()
bfs.bfs(node1)