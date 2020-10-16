n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
def partition(myList, low, high):
    pivot = myList[high]
    i = low-1
    for j in range(low, high):
        if(myList[j]<pivot):
            i += 1
            myList[i],myList[j] = myList[j],myList[i]
    myList[i+1],myList[high] = myList[high],myList[i+1]
    return (i+1)
def quickSort(myList, low, high):
    if(low < high):
        pi = partition(myList, low, high)
        quickSort(myList,low,pi-1)
        quickSort(myList,pi+1,high)
quickSort(myList,0,n-1)
print(myList)