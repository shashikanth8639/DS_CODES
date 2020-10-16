print("enter starting times of activities")
start = list(map(int, input().split()))
print("enter finishing times of activities")
finish = list(map(int, input().split()))
#sorting according to finishing times
#time complexity of sorted() which is trimsort is O(n logn)
finish, start = zip(*sorted(zip(finish, start)))
i = 0
print(start[i])
for j in range(1,len(finish)): #time complexity = O(n-1)
    if(start[j] >= finish[i]):
        print(start[j])
        i += 1
#total time complexity = O(n logn)+ O(n) ==> O(n logn) 
#f(n) = O(g(n)) means that f(n) is a function that atmost
    #grows at the rate o(g(n)) over the long term