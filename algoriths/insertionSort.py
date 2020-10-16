n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
for i in range(1,n):
    key = myList[i]     #element which is being compared with prev element
    j = i-1
    while(j>=0 and myList[j]>key):  #if prev element greater than key, then loop through
        myList[j+1] = myList[j]                            
        j -= 1                      #all prev elemets and replace key with prev element and ....
    myList[j+1] = key
print(myList)                       #prev element place with prev prev element