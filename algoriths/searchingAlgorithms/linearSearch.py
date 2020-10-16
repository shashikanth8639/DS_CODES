n = int(input())
myList = list(map(int, input().rstrip().split()))
x = int(input())
if(x in myList):
    print(myList.index(x))
else:
    print("-1")