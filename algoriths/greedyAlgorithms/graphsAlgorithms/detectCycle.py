# from collections import defaultdict
# class Graph:
#     def __init__(self, v):
#         self.v = v
#         self.graph = defaultdict(list)
#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         self.graph
    
v = int(input())
edgeList = list(map(int, input().split()))
# g = Graph(v)
# for i in edgeList:
#     g.addEdge(i, i+1)
#     i += 1
if(len(edgeList)//2 >= v):
    print("There is a cycle")
else:
    print("No cycle")