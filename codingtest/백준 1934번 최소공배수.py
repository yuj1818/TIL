import sys
input = sys.stdin.readline

def gcd(x, y):
    while y: x, y = y, x%y
    return x

for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))