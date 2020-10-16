'''
    XOR of two opposite signed numbers yields 1 at the most sinificant bit 
'''
n1, n2 = map(int,input().split())
if n1^n2 <0:
    print("They have opposite sings")
else:
    print("They are of same signs")