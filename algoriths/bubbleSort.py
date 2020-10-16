n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
for i in range(n):
    for j in range(n-i-1):                                      #always first two elements are compared, if first 
        if(myList[j] > myList[j+1]):                            #is greater then elemets ae swapped and compares 
            myList[j],myList[j+1] = myList[j+1],myList[j]       #next two elements and so on....
print(myList)                                                   #Here for every loop last elemet gets sorted