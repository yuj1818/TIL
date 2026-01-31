from math import gcd
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
x = gcd(*[a[i] - a[i - 1] for i in range(1, n)])
print((a[-1] - a[0]) // x + 1 - n)