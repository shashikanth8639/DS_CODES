'''
    SELECTION SORT
        This algorithm is based on idea of finding the max or min element
        in an unsorted array and putting it in sorted array

        Time complexity -- O(n**2)
        Auxiliary space complexity -- O(1)
'''

def selectionSort(arr,n):
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    print(arr)
    
n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

selectionSort(arr,n)
print(arr)

'''
    Selection sort is not stable...
    but it can be made stable. Insted of swapping the min element with the current
    element, we have to push all the elements forward for one step and then insert
    the min element at the current position

    The good thing about selection sort is it never makes more than O(n) swaps and 
    can be useful when memory write is a costly operation.
'''