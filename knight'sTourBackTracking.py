def calculateIndegree(visited, a, b, i, j):
    c = 0
    for k in range(8):
        if 0<= i+a[k] < 8 and 0<= j+b[k] <8 and visited[i+a[k]][j+b[k]] == -1:
            c += 1
    return c

def keys(visited, a, b, i, j):
    res = []
    for k in range(8):
        if 0<= i+a[k] < 8 and 0<= j+b[k] <8 and visited[i+a[k]][j+b[k]] == -1:
            ind = calculateIndegree(visited, a, b, i+a[k], j+b[k])
            res.append([ind, i+a[k],j+b[k]])
    res.sort() 
    return res

# def isSafe(visited, i, j):
#     return 0<=i<8 and 0<=j<8 and visited[i][j] == -1

def solveTour(visited, a, b, i, j, pos):
    if pos == 65:
        return True
    # for k in range(8):
    #     if(isSafe(visited, i+a[k], j+b[k])):
    #         visited[i+a[k]][j+b[k]] = pos
    #         if solveTour(visited, a, b, i+a[k], j+b[k], pos+1):
    #             return True
    #         visited[i+a[k]][j+b[k]] = -1
    for k, p,q in keys(visited, a, b, i, j):
        visited[p][q] = pos
        if solveTour(visited, a, b, p, q, pos+1):
            return True
        visited[p][q] = -1
    return False


visited = [[-1]*8 for i in range(8)]
a = [2, 1, -1, -2, -2, -1, 1, 2] 
b = [1, 2, 2, 1, -1, -2, -2, -1]
# print(visited)

visited[3][2] = 1
solveTour(visited, a, b, 3, 2, 2)
print(visited)
