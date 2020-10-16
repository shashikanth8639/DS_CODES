'''
    JUMP SEARCH
        It is performed only on sorted array.
        The basic idea of the jump search is to search fewer elements than
        linear search by jumping ahead of fixed steps instead of searching all
        the elements. If n is the size of an array, then the optimal block size
        to be skipped or to be jumped is sqrt(n) and then check through the array
        at the positions of block size and if the key is less greater than the 
        block size position value then jump to the next block size and continue 
        until the i'th blocksize value which is greater than the key.
            Now perform thr linear search on the elements ehich are in between
            (i-1)th blocksize and i'th blocksize elements( In the worst case we do n/m jumps
        and perform m-1 comparisions)

        (In the worst case we don n/m jumps and m-1 comparisions in the linear search.
        Therefore total number of comparisions in the worst case are ((n/m)+m-1)
        The value of the function ((n/m)+m-1)) will be minimum when m=sqrt(n) )

        Time complexity - O(sqrt(n))
        Auxiliary space complexity - O(1)

        Jump search's time complexity is between linear search and binary search
        i.e,                O(n) > O(sqrt(n)) > O(nlogn)

'''

def doLinearSearch(arr,prev,cur,key):
    for i in range(prev,cur):
        if arr[i] == key:
            print(f"KEY FOUND AT POSITION {i}")
            break
    else:
        print("KEY NOT FOUND")

def jumpSearch(arr,n,key):
    blockSize = int(n**0.5)
    for i in range(0,n,blockSize):
        if key <= arr[min(i+blockSize,n-1)]:
            currentBlock = i+blockSize
            doLinearSearch(arr,currentBlock-blockSize,currentBlock,key)
            break

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))

arr.sort()
jumpSearch(arr,n,key)


'''
    Binary Search is better than Jump Search, but Jump search has an advantage
    that we traverse back only once (Binary Search may require up to O(Log n) jumps,
    consider a situation where the element to be searched is the smallest element or 
    smaller than the smallest). So in a system where binary search is costly,
    we use Jump Search.
'''