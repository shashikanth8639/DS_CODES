n = int(input())
print("Enter array elements in one line")
myList = list(map(int, input().rstrip().split()))
def bubble_sort(myList):
    for i in range(n)