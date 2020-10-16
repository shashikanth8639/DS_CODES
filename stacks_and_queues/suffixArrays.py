#Initialization phase
def sortCharacters(s):
    n=len(s)
    order=[0]*n
    count=[1]+[0]*(26)
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
    return order

def computeCharClasses(s, order):
    n=len(s)
    cs = [0]*n
    cs[order[0]]=0
    for i in range(1,n):
        if s[order[i]] != s[order[i-1]]:
            cs[order[i]]=cs[order[i-1]]+1
        else:
            cs[order[i]]=cs[order[i-1]]
    return cs

def sortDoubled(s,l,order,cs):
    n=len(s)
    count=[0]*n
    newOrder = [0]*n
    for i in range(n):
        count[cs[i]]+=1
    for i in range(1,n):
        count[i]+=count[i-1]
    # print(count,cs)
    for i in range(n-1,-1,-1):
        start = (order[i]-l+n)%n
        cl = cs[start]
        count[cl]-=1
        newOrder[count[cl]]=start
    # print(newOrder)
    return newOrder

def updateCs(newOrder,cs,l):
    n=len(newOrder)
    newClass = [0]*n
    newClass[newOrder[0]]=0
    c=0
    for i in range(1,n):
        cur=newOrder[i]
        prev=newOrder[i-1]
        mid=(cur+l)%n
        midPrev = (prev+l)%n
        if cs[cur]!=cs[prev] or cs[mid]!=cs[midPrev]:
            c+=1
        newClass[cur]=c
    return newClass

def invertSuffixArray(order):
    pos = [0]*len(order)
    for i in range(len(order)):
        pos[order[i]]=i
    return pos
def lcpOfSuffixes(s,i,j,equal):
    lcp = max(0,equal)
    n=len(s)
    while i+lcp <n and j+lcp<n:
        if s[i+lcp]==s[j+lcp]:
            lcp+=1
        else:
            break
    return lcp
def computeLCPArray(s,order):
    n=len(s)
    lcpArray=[0]*(n-1)
    lcp=0
    posInOrder = invertSuffixArray(order)
    suffix = order[0]
    for i in range(n):
        orderIndex = posInOrder[suffix]
        if orderIndex == n-1:
            lcp=0
            suffix = (suffix+1)%n
            continue
        nextSuffix = order[orderIndex+1]
        lcp = lcpOfSuffixes(s,suffix,nextSuffix,lcp-1)
        lcpArray[orderIndex]=lcp
        suffix = (suffix+1)%n
    return lcpArray

    

# s='ababbab$' 
s='azaza$'

#Building Suffic array
n=len(s)
order = sortCharacters(s)
cs = computeCharClasses(s,order)
l=1
# print(order)
while l<n:
    order = sortDoubled(s,l,order,cs)
    cs = updateCs(order,cs,l)
    l*=2
print(order)
lcp = computeLCPArray(s, order)
print(lcp)