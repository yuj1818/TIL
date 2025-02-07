import sys
input = sys.stdin.readline

def plus(num, x):
    if x == 1: return num % 1000000007
    if  x % 2 == 0:
        v = plus(num, x / 2)
        return v * v % 1000000007
    else:
        v = plus(num, (x - 1) / 2)
        return num * v * v % 1000000007

k, p, n = map(int, input().split())
print(k * plus(p, n * 10) % 1000000007)