'''
    TERNARY SEARCH
        It works on sorted arrays.
        It is a divide and conquer algorithm which is used to find an element
        in an array. It is similar to binary search, but here we divide the 
        array into three parts and determine which has the key element by taking
        mid1 and mid2, where
                            mid1 = start+(end-1)//3
                            mid2 = end-(end-1)//3
        first we compare the key with mid1 if equal we return else
        we compare key with mid2 if matches then return else we 
        chech wether the key is less than mid1 then do ternary search on
        first part els if key > mid1 and key <= mid2 then perfomr ternary
        search on second part else perform ternary search on the last part
        of the array
        Time complexity -- O(log3n)
        Auxiliary space complexity -- O(1)
'''
def ternarySearch(arr,n,key):
    start = 0
    end = n-1
    print(arr)
    while start <= end:
        mid1 = start+(end-start)//3
        mid2 = end-(end-start)//3
        if arr[mid1] == key:
            print(f"KEY FOUND AT POSITION {mid1}")
            return
        if arr[mid2] == key:
            print(f"KEY FOUND AT POSITION {mid2}")
            return
        if key < arr[mid1]:
            print("IM LESS",arr[mid1])
            end = mid1-1
        elif key > arr[mid2]:
            print("IM BETWEEN",arr[mid2])
            start = mid2+1
            print(start,"njdknvj")
        else:
            start = mid1+1
            end = mid2-1
    print("KEY NOT FOUND")
    return


n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))

arr.sort()
ternarySearch(arr,n,key)