'''
    last bit is always one for odd numbers(so just and it with 1)
    and it is zero for even numbers.
'''
n = int(input())
if((n&1)==1):
    print("NUmbere is odd")
else:
    print("Number is even")