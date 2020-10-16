'''
    LINEAR SEARCH
        It works on sorted and unsorted arrays
        Searching through all the elements of the array one by one.
        Time complexity - O(n)
        Auxiliary Space complexity - O(1)
'''

def linearSearch(arr,n):
    for position,element in enumerate(arr):
        if key == element:
            print(f"KEY FOUND AT POSITION {position}")
            return
    print("KEY NOT FOUND")

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
key = int(input("Enter the key to be searched: \n"))

linearSearch(arr,n)

'''
    ---SENTINEL LINEAR SEARCH---

        There is a modified version of linear search called SENTINEL LINEAR SEARCH
    (not in terms of time complexity which is O(n) but in terms of number of 
    comparisons **Not much difference when used in python). When you use 'range in 
    python or traditional for loop in other programming languages' for looping 
    through elements of list or array, each time a comparision is made in for loop
    to check whether the index is out of bounds which is an extra overhead. In order 
    to reduce it, we generally add the key(which is going to be searched) at the end
    of the array and the loop through the array while array element is not equal to 
    the key , the check whether the index is in range of n and print the appropriate
    results  

    arr[n] = key
    i = 0
    while(arr[i] != key):
        i += 1
    print("KEY FOUND" if i!=n else "KEY NOT FOUND)

    SENTINEL: like guard, whose job is to stand and keep watch
'''

'''
    Auxiliary space complexity -- is the extra space ot temporary space used by the
    algorithms                      'where as'
    Space complexity --  is the total space used by the algorithm with respect to 
    the input size. 
'''