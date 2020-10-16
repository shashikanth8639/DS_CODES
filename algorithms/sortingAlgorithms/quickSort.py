
def partition(arr,p,q):
    pivot = arr[q]
    i = p-1
    for j in range(p,q):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[q] = arr[q],arr[i+1]
    return i+1



def quickSort(arr,start,end):
    if start < end:
        r = partition(arr,start,end)
        quickSort(arr,start,r-1)
        quickSort(arr,r+1,end)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
quickSort(arr,0,n-1)
print(arr)