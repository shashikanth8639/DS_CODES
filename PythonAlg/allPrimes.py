def prime(n):
    if n%2 == 0:
        return " not prime"
    else:
        for i in range(3,n-1,2):
            if n%i == 0:
                return " not prime"
    return "prime"
n = int(input("Enter number of primes to be displayed: "))
res = 0
count = 1
i = 3
print("2")
while count <= 10:
    res = prime(i)
    if res == "prime":
        count += 1
        print(i)
    i += 2
    
