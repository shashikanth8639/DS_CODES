from heapq import heappush,heappop,heapify
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[]
        heapify(self.graph)
    
    def addEdge(self,u,v,w):
        heappush(self.graph,(w,u,v))
    
    def find(self,rep,i):
        if rep[i]!=i:
            rep[i]=self.find(rep,rep[i])
        return rep[i]
    
    def union(self,rep,rank,x,y):
        if rank[x]>rank[y]:
            rep[y]=x
        elif rank[y]>rank[x]:
            rep[x]=y
        else:
            rep[y]=x
            rank[x]+=1

    def kruskalMinSpan(self):
        rep=[i for i in range(self.v)]
        rank=[1]*self.v
        e=0
        res=[]
        while e<self.v and self.graph!=[]:
            w,u,v = heappop(self.graph)
            # print(w,u,v)
            x = self.find(rep,u)
            y = self.find(rep,v)
            if x!=y:
                e+=1
                res.append([u,v,w])
                self.union(rep,rank,x,y)
        for u,v,w in res:
            print(u,'--',v,'==',w)

# g=Graph(4)
# g.addEdge(0, 1, 10) 
# g.addEdge(0, 2, 6) 
# g.addEdge(0, 3, 5) 
# g.addEdge(1, 3, 15) 
# g.addEdge(2, 3, 4) 
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
graph.kruskalMinSpan()



