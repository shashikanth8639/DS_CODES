#code
from collections import defaultdict


def ap(graph,u,lid,parent,low,visited):
    connected=0
    # print(visited,'beff')
    visited.remove(u)
    # print(visited,'remmm')
    low[u]=lid
    for each in graph[u]:
        if each==parent[u]:
            continue
        if each in visited:
            parent[each]=u
            connected+=1
            if ap(graph,each,lid+1,parent,low,visited):
                return True
        low[u] = min(low[u],low[each])
        if lid<=low[each] and parent[u]!=-1:
                return True
        if parent[u]==-1 and connected>1:
            return True
    # print('curr',u)
    return False


t=int(input())
while t>0:
    n,e=map(int, input().split())
    graph=defaultdict(list)
    l=list(map(int, input().split()))
    ans=1
    lid=0
    low=[0]*n
    parent=[-1]*n
    visited = {i for i in range(n)}
    for i in range(0,2*e,2):
        graph[l[i]].append(l[i+1])
        graph[l[i+1]].append(l[i])
    # print(visited)
    print(l)
    print(graph)
    parent[0]=-1
    print(ap(graph,0,lid,parent,low,visited))
    # print(visited)
    # print(ans)
        
    t-=1