def firstOrder(s):
    n=len(s)
    order=[0]*n
    cs=[0]*n
    count=[1]+[0]*26
    for i in range(n-1):
        count[ord(s[i])-96]+=1
    for i in range(1,27):
        count[i]+=count[i-1]
    for i in range(n-2,-1,-1):
        c=ord(s[i])-96
        count[c]-=1
        order[count[c]]=i
    count[0]=0
    order[0]=n-1
    cs[order[0]]=0
    c=0
    for i in range(1,n):
        if s[order[i]]!=s[order[i-1]]:
            c+=1
        cs[order[i]]=c
    return order,cs
def sortDoubleAndClassUpdate(s,order,l,cs):
    n=len(s)
    count=[0]*n
    newOrder=[0]*n
    for i in range(n):
        count[cs[i]]+=1
    for i in range(1,n):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        start = (order[i]-l+n)%n
        cl = cs[start]
        count[cl]-=1
        newOrder[count[cl]]=start
    newClass = [0]*n
    newClass[newOrder[0]]=0
    c=0
    for i in range(1,n):
        cur=newOrder[i]
        prev=newOrder[i-1]
        mid,midPrev=(cur+l)%n, (prev+l)%n
        if cs[cur]!=cs[prev] or cs[mid]!=cs[midPrev]:
            c+=1
        newClass[cur]=c
    return newOrder,newClass

# s='ababbab$' 
s='azaza$'
order,cs = firstOrder(s)
l=1
while l<len(s):
    order,cs = sortDoubleAndClassUpdate(s,order,l,cs)
    l*=2
print(order)

    