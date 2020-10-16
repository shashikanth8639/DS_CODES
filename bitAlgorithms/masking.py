n,k = map(int, input().split())

'''
    clearing kth bit. Take 1 and left shift it by k-1 times and then INVERT it
    and do AND with n.
'''
print('After clearing kth bit: ',n&~(1<<(k-1)))

'''
    Turning on / setting kth bit. Take 1 and left shift it by k-1 times and then
    do OR with n.
'''
print('After setting kth bit: ',n|(1<<(k-1)))

'''
    checking kth bit. Take 1 and left shift it by k-1 times and then
    do AND with n.
'''
print('checking kth bit: ',n&(1<<(k-1))!=0)
