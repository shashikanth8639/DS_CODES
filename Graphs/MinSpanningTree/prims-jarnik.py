from heapq import heappop,heapify,heappush
from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph = defaultdict(list)
        # self.graph={}
        # for i in range(self.v):
        #     self.graph[i]=[]
        #     heapify(self.graph[i])

    def addEdge(self,u,v,w):
        self.graph[u].append((w,v))
        self.graph[v].append((w,u))
        # heappush(self.graph[u],(w,v))
        # heappush(self.graph[v],(w,u))
    
    def primsJarnik(self):
        # heap=[]
        # d=defaultdict(set)
        res=[]
        # heapify(heap)
        # heap.heappush(0)
        # visited=set()
        visited={0}
        st = 0
        edges = [(w,st,end) for w,end in self.graph[st]]
        heapify(edges)
        e=0
        while e<self.v and edges!=[]:
            w,u,v = heappop(edges)
            if v not in visited:
                visited.add(v)
                e+=1
                res.append((u,v,w))
                # d[u]=v
                for w,end in self.graph[v]:
                    if end not in visited:
                        heappush(edges,(w,v,end))
            # e+=1
        # print(d)
        print(res)
        # e=0

        # while e<self.v and heap!=[]:
        #     u=heappop(heap)
graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7)
graph.primsJarnik() 
