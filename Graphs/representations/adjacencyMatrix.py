'''
    Space complexity is O(V**2)
    Time complexity:
        for removing an edge is O(1)
        for querying an edge is O(1)
        for adding a vertex is O(v**2)
    Disadvantages:
        It takes more space for even sparse graphs which may have fewer edges
        Adding a new vertex takes too much time
    It is most suitable for dense graphs
'''

class Graph:

    def __init__(self,v):
        #Initializing number of vertices and the adjacency matrix
        self.v = v
        self.graph = [[0]*self.v for i in range(self.v)]
    
    def addEdge(self,u,v):
        #Adding edge from vertex u to v
        self.graph[u][v]=1
        self.graph[v][u]=1 #since the graph is undirected.
    
    def displayEdges(self):
        '''Displaying all the edges. This is just bad displaying beacuse we are
            displaying all the edges. Inorder to display the edges properly we 
            can use dfs or bfs traversals of graph'''
        for i in range(self.v):
            for j in range(self.v):
                if self.graph[i][j]==1:
                    print(i,'-->',j)
    
    def removeEdge(self,u,v):
        #Removing an edge
        self.graph[u][v]=0
    

graph = Graph(5)
graph.addEdge(0, 1) 
graph.addEdge(0, 4) 
graph.addEdge(1, 2) 
graph.addEdge(1, 3) 
graph.addEdge(1, 4) 
graph.addEdge(2, 3) 
graph.addEdge(3, 4)

graph.displayEdges()