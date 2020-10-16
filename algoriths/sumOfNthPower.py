def sumofnthpowers(x,n,cur_num = 1, cur_sum = 0):
    res = 0
    p = cur_num**n
    while(p+cur_sum < x):
        res += sumofnthpowers(x,n,cur_num+1,p+cur_sum)
        cur_num += 1
        p = cur_num**n
    if(p+cur_sum == x):
        res = res+1
    return res
x = int(input())
n = int(input())
count = sumofnthpowers(x,n)
print(count)
