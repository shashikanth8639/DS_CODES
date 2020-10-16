t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    maxS = 1
    maxele = 0
    for i in range(n-1):
        if maxele ==0 or arr[i]<maxele:
            c = 1
            j = i+1
            m = arr[i]
            while j<n:
                if arr[j]> m:
                    m = arr[j]
                    c += 1
                j += 1
            maxS = max(maxS,c)
            maxele = arr[i]
        else:
            print("HH",arr[i])
        
    print(maxS)
    t-=1