def lis(arr,n,i,maxi,ele=None):
    # a=True
    if i>n:
        return 0
    if ele is None:
        ele =arr[i]
    if i==n:
        if arr[i]>=ele:
            return 1
        return 0
    
    c1=c2=c3=0
    if arr[i+1]>=ele:
        c1 = 1+lis(arr,n,i+1,maxi,arr[i+1])
        # c2 = 1+lis(arr,n,i+1,maxi,ele)
    # else:
    c2 = lis(arr,n,i+1,maxi,ele)
    c3 = lis(arr,n,i+1,maxi)
    maxi[0] = max(maxi[0],c1,c2,c3)
    # return 1+max(c1,c2)
    return max(c1,c2)

t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = [-999999]
    lis(arr,n-1,0,maxi)
    print(maxi[0])
    t-=1