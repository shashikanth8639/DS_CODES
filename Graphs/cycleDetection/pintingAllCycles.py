from collections import defaultdict
class Graph:

    def __init__(self,v):
        self.v=v
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfsUtil(self,u,visited,stack,parent):
        print(*stack,'aa',u,'start')
        visited[u]=1
        stack.append(u)
        for each in self.graph[u]:
            print('parent',u,'child',each)
            if visited[each]==-1:
                self.dfsUtil(each,visited,stack,u)
            elif not(visited[each]==0 and visited[u]==0) and parent!=each:
                i = stack.index(each)
                print(*stack[i:],end=" cycle\n")
                for j in stack[i:]:
                    stack.pop()
                    visited[j]=0
                # stack = stack[:i].copy()
                # print(*stack,end=" after\n")

    def dfs(self):
        visited=[-1]*self.v
        stack=[]
        for i in range(self.v):
            if visited[i]==-1:
                self.dfsUtil(0,visited,stack,-1)
g = Graph(6)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(0,4)
g.addEdge(4,5)
g.addEdge(5,0)
g.dfs()
g = Graph(14)
g.addEdge(0,1)
g.addEdge(1, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 
g.addEdge(4, 6) 
g.addEdge(4, 7) 
g.addEdge(5, 6) 
g.addEdge(3, 5) 
g.addEdge(7, 8) 
g.addEdge(6, 10) 
g.addEdge(5, 9) 
g.addEdge(10, 11) 
g.addEdge(11, 12) 
g.addEdge(11, 13) 
g.addEdge(12, 13) 

g.dfs()