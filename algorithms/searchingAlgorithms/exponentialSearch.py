'''
    EXPONENTIAL SEARCH
        It is kind of like jump search(In terms of process).In this search we 
        perform two steps:
            1.find the range where the key is located,then
            2.perform binary serach over the range
        Range- first we start with the ideal subarray of size 1, then we try the sizes
        2,4,8....which is exponential unitl the last element of subarray is not greater
        Once we find the index whose value is grater than key, then we perform binary
        search over elements between arr[i//2] and arr[i]

        Time complexity -- O(log n)
        Auxiliary space search -- O(1) when itertative binary search used else O(n)
'''
def binarySearch(arr,start,end,key):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            print(f"KEY FOUND AT POSITION {mid}")
            return
        if key < arr[mid]:
            end = mid
        else:
            start = mid+1
    print("KEY NOT FOUND")

def exponentialSearch(arr,n,key):

    i = 1
    if arr[0] == key:
        print(f"KEY FOUND AT POSITION {i}")
        return
    while i<n and key > arr[i]:
        i = i*2
    print(i,n)
    binarySearch(arr, i//2, min(i,n), key)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))

arr.sort()
exponentialSearch(arr,n,key)

'''
    Exponential binary search is useful for unbounded searches, where the size of the
    array is infinite
    It even works better than binary search for bounded arrays and also when the 
    element is closer to the first element
'''