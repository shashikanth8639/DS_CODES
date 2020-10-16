from collections import defaultdict
from heapq import heappop, heappush

g = defaultdict(list)

n = int(input())
for i in range(n):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)