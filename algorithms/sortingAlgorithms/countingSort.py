
def countingSort(arr,n):
    maxi = max(arr)
    mini = min(arr)
    s = maxi-mini+1
    output = [""]*(s)
    count = [0]*(s)

    
    for each in arr:
        count[each-mini] +=1

    j = 0
    for i in range(mini, maxi+1):
        while count[i-mini] >0:
            arr[j] = i
            j+=1
            count[i-mini] -=1
    print(arr)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
# arr = input().strip()

countingSort(arr,n)
# print(arr)