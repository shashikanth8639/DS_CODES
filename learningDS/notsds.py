n,e = map(int,input().strip().split())
d = {}
for i in range(e):
    u,v = map(int,input().strip().split())
    try:
        d[u].append(v)
    except:
        d[u] = [v]
    try:
        d[v].append(u)
    except:
        d[v] = [u]
for key in sorted(d):
        print(*sorted(d[key]),sep="->")
