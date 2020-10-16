from collections import defaultdict

'''
    Space complexity is O(|V|+|E|) ----|V|= set of vertices
    Time complexity:
        for removing an edge is O(V)
        for querying an edge is O(V)
        for adding a vertex is O(1)
    It is the most commonly used representation of graphs
    It is well suitable for sparse graphs
'''

class Graph:

    def __init__(self,v):
        #Initializing number of vertices and the adjacencyList(dictionary in python)
        self.v = v
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        #Adding an edge from vertex u to v which takes O(1) time complexity
        #If it is weighted graph add tuple of toVertex and weight
        self.graph[u].append(v)
        self.graph[v].append(u) #since it is an undirected graph
    
    def displayEdges(self):
        '''Displaying all the edges. This is just bad displaying beacuse we are
            displaying all the edges. Inorder to display the edges properly we 
            can use dfs or bfs traversals of graph'''
        for u in self.graph:
            for v in self.graph[u]:
                print(u,'-->',v)
    
    def removeVertex(self,u):
        #Removing an edges takes O(V) time complexity
        del self.graph[u]
        for v in self.graph:
            try:
                self.graph[v].remove(u)
            except: pass
        print("vertex was removed")
    
    def removeEdge(self,u,v):
        #removing an edge takes O(1) time
        try:
            self.graph[u].remove(v)
        except: pass
        try:
            self.graph[v].remove(u)
        except: pass
    
    def displayPath(self,u,v,stack,notVisited):
        stack.append(u)
        notVisited.remove(u)
        if u==v:
            return True
        for each in self.graph[u]:
            if each in notVisited:
                return self.displayPath(each,v,stack,notVisited)
        return False

    def path(self,u,v):
        #It is not hte shortes path.
        stack=[]
        notVisited={i for i in range(self.v)}
        if self.displayPath(u,v,stack,notVisited):
            print(*stack,sep="-->")
        else:
            print("No path found")

graph = Graph(5)
graph.addEdge(0, 1) 
graph.addEdge(0, 4) 
graph.addEdge(1, 2) 
graph.addEdge(1, 3) 
graph.addEdge(1, 4) 
graph.addEdge(2, 3) 
graph.addEdge(3, 4)

graph.displayEdges()
print("Paths")
graph.path(0,3)
# graph.removeVertex(4)
# graph.removeEdge(0,1)

# graph.displayEdges()

