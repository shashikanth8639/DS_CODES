
def getDigit(num,pos):
    s = str(num)
    if pos <= len(s):
        return int(s[-pos])
    else:
        return 0
    # print(num//pos%10)
    # return num//10*pos%10

def countingSort(arr,n,pos):
    
    out = [0]*n
    count = [0]*10
    for i in range(n):
        index = getDigit(arr[i],pos)
        count[index] +=1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        index = getDigit(arr[i],pos)
        out[count[index]-1] = arr[i] 
        count[index] -= 1
    for i in range(n):
        arr[i] = out[i]
        
def radixSort(arr,n):   
    m = max(arr)
    pos = 0
    while m>0:
        pos += 1
        countingSort(arr,n,pos)
        # digitBucket = [[] for i in range(10)]
        # for each in arr:
        #     digitBucket[getDigit(each,pos)].append(each)
        # arr = [item for sublist in digitBucket if sublist != [] for item in sublist]
        m //= 10
    print(arr)
    
    # return arr

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))

radixSort(arr,n)
# arr = radixSort(arr,n)
# print(arr)