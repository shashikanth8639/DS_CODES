'''
    INSERTION SORT
        We divide the given array into two parts sorted and unsorted
        Then we pick the first element from the unsorted array and place
        it in the sorted array in its correct position. Repeat this
        until unsorted array is empty.

        Time complexity -- O(n*n)
        Auxiliary space complexity -- O(1)
'''

def insertionSort(arr,n):
    for i in range(1,n):
        j = i
        temp = arr[i]
        while arr[j-1]>temp and j>0:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    print(arr) 

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

insertionSort(arr,n)
print(arr)

'''
    Insertion sort is mainly used when there is continuoua flow of data
    and we want to keep them sorted.
    
    Insertion sort is used when number of elements is small. It can also
    be useful when input array is almost sorted, only few elements are 
    misplaced in complete big array.
'''