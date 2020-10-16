'''
    BINARY SEARCH
        It is used only on sorted arrays.First we search for the middle element,
        if it is equal to the key then return else if the key is less than
        the middle element then do binary search on the first half of the array(Here we are 
        eliminating serach in the half of the array which is second part) else if key
        is greater than the mid value then do binary search in the second part of the array
        
        Iterative Approach---- 
        Time complexity - O(logn)
        Space complexity - O(1)

        Recursive Approach--- For recursive approach system uses its internal
                space for call stack
        Time complexity - O(logn)
        Space complexity - O(logn)
'''

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))
arr.sort()

# Iterative approach
def binarySearchIterative(arr,n):
    start,end = 0,n
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            print(f"KEY IS FOUND AT POSITION {mid}")
            return
        elif key < arr[mid]:
            end = mid
        else:
            start = mid+1
    print("KEY NOT FOUND")

# Recursive Approach
def binarySearchRecursive(arr,key,start,end):
    if start <= end:
        mid = (start+end)//2
        # if key equals mid value then return
        if arr[mid] == key:
            print(f"KEY FOUND AT POSITION {mid}")
            return
        # if key is less than mid value the search in the first part of the array
        if key < arr[mid]:
            return binarySearchRecursive(arr,key,start,mid-1)
        # if key is greater than mid value the search in the second part of the array
        else:
            return binarySearchRecursive(arr,key,mid+1,end)
    else:
        print("KEY NOT FOUND")
        return
if arr[0] <= key and key <= arr[-1]:
    # binarySearchIterative(arr,n)
    binarySearchRecursive(arr,key,0,n-1)
else:
    print("KEY NOT FOUND")
