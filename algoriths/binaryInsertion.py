n = int(input())
myList = list(map(int, input().rstrip().split()))
def binary_search(myList, key, start, end):
    if(start == end):
        if(myList[start]>key):
            return start
        else:
            return start+1
    mid = (start + end)/2
    if(key == mid):
        return mid
    if(key > mid):
        return binary_search(myList, key, mid+1, end)
    if(key < mid):
        return binary_search(myList, key, start, mid-1)
for i in range(1, n):
    key = myList[i]
    j = binary_search(myList, key, 0, i-1)
    myList = myList[:j] + [key] + myList[j:i] + myList[(i+1):]
    # myList = myList[:1] + [key] + myList[1:2] + myList[(1+1):]
print(myList)