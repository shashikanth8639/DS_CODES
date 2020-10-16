'''
    BUBBLE SORT
        It is the simplest sorting algorithm which works by repeatedly
        swapping the adjacent elements if they are in wrong order.
        After first loop the first element gets replaced with the
        min element of the array (last for max case) and for next
        loop the second positions gets filled with the second min
        element and ... unitl the last element.

        Time complexity -- O(n*n) for worst and avg, O(n) for best case
        Auxiliary space complexity -- O(1)
'''
#**** when array is already sorted, the below code runs in O(n*n) time.
# inorder to improve it, if an inner loop doesn't cause any swapping then
# break out of the loop because the array is already sorted.

def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

bubbleSort(arr,n)
