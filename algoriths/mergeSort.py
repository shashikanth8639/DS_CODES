n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
def merge_sort(myList):
    n = len(myList)
    if(n>1):
        mid = n//2
        l = myList[:mid]
        r = myList[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                myList[k] = l[i]
                i += 1
            else:
                myList[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            myList[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            myList[k] = r[j]
            j += 1
            k += 1   
merge_sort(myList)
print(myList)