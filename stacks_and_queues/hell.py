from collections import defaultdict
n = int(input())
m = int(input())
s = input().strip()
x = list(map(int, input().split()))
y = list(map(int, input().split()))
l = [-1]

d = defaultdict(list)
for i in range(m):
	d[x[i]].append(y[i])

def dfs(d, i, visited, rs, s, res, l):
	visited.add(i)
	rs.add(i)
	l[0] = max(l[0], res.count(max(res, key=res.count)))
	for ele in d[i]:
		if ele not in visited:
			if dfs(d, ele, visited, rs, s, res+s[ele-1], l) == 0:
				return 0
		elif ele in rs:
			return 0
	rs.remove(i)
	return 1

visited = set()
rs = set()
for i in range(1, n+1):
	if i not in visited and dfs(d, i, visited, rs, s, s[i-1], l) == 0:
			print(-1)
			break
else:
	print(l[0])
