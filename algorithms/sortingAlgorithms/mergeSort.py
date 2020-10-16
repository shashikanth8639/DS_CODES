'''
    MERGE SORT
        It is a divide and conquer algorithm. Here we divide the array
        into two halves and keep on breaking them until they become
        too small to be broken
        Then each of these broken pieces are merged together along with sorting
        to inch towards the final answer.

        Time complexity -- O(nlogn)
        Auxiliary space complexity -- O(n)
'''

def merge(arr,p,q,r):   
    arr1 = arr[p:q]
    arr2 = arr[q:r+1]
    i = j = 0
    print(arr1[i],arr2[j])
    print(p,r)
    k = p
    while i< len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr[k] = arr2[j]
            j += 1
        else:
            arr[k] = arr1[i]
            i += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        i +=1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k += 1
    print("MODIFIED ARRY IS ",arr)
def mergeSort(arr,start,end):
    if start < end:
        mid = (start+end)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid+1,end)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

mergeSort(arr,0,n-1)
print(arr)

'''
    Merge sort is used for sorting linked lists in O(nlogn) time
    Java 6 and earlier versions used merge sort as their sorting algorithm
    It is also used in EXTERNAL SORTING.
'''