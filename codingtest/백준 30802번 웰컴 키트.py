import math

n = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())

shirt = 0

for size in sizes:
    shirt += math.ceil(size / t)

print(shirt)
print(n // p, n % p)