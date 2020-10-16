from collections import defaultdict
class Graph:

    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.low = {}
        self.visited = set()
        self.art = []
        self.bridges = []
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, id, parent, node):
        self.low[node] = id
        self.visited.add(node)

        for v in self.graph[node]:
            if v == parent: continue

            if v not in self.visited:
                self.dfs(id+1, node, v)
            
            self.low[node] = min(self.low[node], self.low[v])

            if id < self.low[v]:
                self.bridges.append([node, v])
            

    def displayBridges(self):
        self.dfs(0, -1, 0)
        return self.bridges

    def dfsutil(self, id, parent, node):
        self.low[node] = id
        self.visited.add(node)
        numEdges = 0

        for v in self.graph[node]:
            if v == parent: continue

            if v not in self.visited:
                numEdges += 1
                self.dfsutil(id+1, node, v)
            
            self.low[node] = min(self.low[node], self.low[v])

            if id <= self.low[v] and parent != -1:
                self.art.append(node)
        
        if parent == -1 and numEdges > 1:
            self.art.append(node)


    def displayArticulationPoints(self):
        self.visited = set()
        self.dfsutil(0, -1, 0)
        return self.art

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(1, 3)

print(g.displayBridges())
print(g.displayArticulationPoints())
