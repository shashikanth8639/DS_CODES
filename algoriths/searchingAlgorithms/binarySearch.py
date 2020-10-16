def binarySearch(inList,x):
    l = len(inList)
    mid = l//2
    print(mid)
    if(x == inList[mid]):
        print(myList.index(x))
    elif(x > inList[mid]):
        return binarySearch(inList[mid+1:], x)
    else:
        return binarySearch(inList[:mid], x)
myList = list(map(int, input().strip().split()))
myList.sort()
x = int(input())
binarySearch(myList, x)
