def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input())

p = 0
for n in range(2, 104):
    if isPrime(n):
        if n * p > num:
            print(n * p)
            break
        p = n