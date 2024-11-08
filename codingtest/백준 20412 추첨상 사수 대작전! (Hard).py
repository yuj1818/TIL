import sys
m, seed, x1, x2 = map(int, sys.stdin.readline().split())
a = (x1 - x2) * pow(seed - x1, m-2, m) % m
c = (x1 - (a * seed)) % m
print(a, c)