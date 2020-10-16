myList1 = list(map(int, input().split()))
myList2 = list(map(int, input().split()))
def compareSublist(list1, list2):
    count = 0
    a = len(list1)
    b = len(list2)
    if(list1 == list2):
        return True
    if(a > b):
        return False
    else:
        for i in range(a):                  #for i in range(b):if(l[i] == s[0]):while(l )
            if(list1[i] == list2[i]):
                count += 1
                if(count == a):
                    return True
            else:
                return compareSublist(list1, list2[1:])
                
    return False
if(compareSublist(myList1, myList2)):
    print("List found")
else:
    print("List not found")
    