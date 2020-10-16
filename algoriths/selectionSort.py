n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
for i in range(n):
    min = myList[i]                          #Initially first element is considered as min and compared with
    for j in range(i+1,n):
        if(min > myList[j]):                 #all other elements and (i)th value replaces with min.. and loop so on
            min,myList[j] = myList[j],min
    myList[i] = min                          # All the left side of the min element are sorted i.e two arrays
print(myList)                                #sorted on left and unsorted on right