'''
    Interpolation is used for sorted array in which the values are 
    uniformly distributed.It is an improvement over binary search.
    Binary search always goes to the middle element whereas interpolation
    search may goes to the differernt locations based on the value of the
    key to be searched (if the value of the key is closer to the last element, 
    interpolation search is likely to start search toward the end side)
        To find the position to be searched we use the formula
                            ___                                                 ___
                           |                                                       |
                           |    (key - arr[startIndex]) * (startIndex - endIndex)  |
        pos = startIndex + |    _________________________________________________  |
                           |            arr[startIndex] - arr[endIndex]            |
                           |___                                                 ___|
    First we check wether the element at pos is equal to the key if yes then return
    else if key < pos the decrement pos(i.e, check the element prior to the pos)
    else increment pos(check the element which is next to pos) and continue till 
    start index <= end Index

    Time complexity -- O(log logn) (In worst case it can take upto O(n))
    Auxiliary space complexity -- O(1) 
'''
def calculatePosition(start,end,key):
    return start + int(((key - arr[start])*(start-end))/(arr[start]-arr[end]))

def interpolationSearch(arr,n,key):
    startIndex = 0
    endIndex = n-1
    pos = 0
    if key > arr[-1] or key < arr[0]:
        print("KEY NOT FOUND")
        return
    while startIndex <= endIndex:
        
        pos = calculatePosition(startIndex, endIndex, pos)

        if key == arr[pos]:
            print(f"KEY FOUND AT POSITION {pos}")
            return
        if key < arr[pos]:
            endIndex -= 1
        else:
            startIndex += 1  
    print("KEY NOT FOUND")
    return

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))

arr.sort()
interpolationSearch(arr,n,key)