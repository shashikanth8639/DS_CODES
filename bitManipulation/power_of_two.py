import math
#Find if a number if power of 2

def is_power_of_two(num):
    return num > 0 and num & num-1 == 0

def is_power_of_two_using_log(num):
    return num>0 and math.log2(num) == math.trunc(math.log2(num))

def is_power_of_two_using_modulue(num):
    if num < 1: return False
    while num%2 == 0:
        num //= 2
    return num == 1


print(is_power_of_two(45))
print(is_power_of_two(1024))
print(is_power_of_two_using_modulue(45))
print(is_power_of_two_using_modulue(1024))
print(is_power_of_two_using_log(45))
print(is_power_of_two_using_log(1024))