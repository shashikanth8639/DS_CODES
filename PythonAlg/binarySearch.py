n = int(input("Enter number of elements: "))
myList = list(map(int, input().strip().split()))
ele = int(input("Enter the element to be searched: "))
myList.sort()
def binarySearch(inpList, ele):
    while(len(inpList) > 1):
        l = len(inpList)
        mid = l//2 - 1 if l%2 == 0 else l//2
        if ele == inpList[mid] :
            print("ele=mid")
            return  1
        elif ele > inpList[mid]:
            inpList = inpList[mid+1:]
        else:
            inpList = inpList[:mid]
    if len(inpList) == 1 and ele == inpList[0]:
        return 1
    return -1
# def binarySearch(inpList, ele):
#     l = len(inpList)
#     while(l > 1):
#         mid = l //2 - 1
#         if inpList[mid] == ele:
#             return  1
#         elif ele > inpList[mid]:
#             return binarySearch(inpList[mid+1:], ele)
#         else:
#             return binarySearch(inpList[:mid], ele)
#     return -1

res = binarySearch(myList, ele)
if(res == 1):
    print("Elememt is found")
else:
    print("Element not found")