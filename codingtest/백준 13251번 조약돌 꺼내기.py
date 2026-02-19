from math import comb
import sys

input = sys.stdin.readline
m = int(input())
colors = list(map(int, input().split()))
n = sum(colors)
k = int(input())
print(sum([comb(x, k) for x in colors]) / comb(n, k))
