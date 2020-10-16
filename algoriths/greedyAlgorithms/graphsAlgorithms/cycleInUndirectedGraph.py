#### Disjoint set or Union-Find algorithm ####
from collections import defaultdict
#default dict doesn't give key error..if there is no key which we are calling.
class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    

v = int(input())
edgesList = list(map(int, input().split()))

