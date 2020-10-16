n = int(input())
myList = list(map(int, input().rstrip().split()))
x = int(input())
def search(x):
    if(x in myList):
        search(x*2)
    else:
        print(x)
search(x)