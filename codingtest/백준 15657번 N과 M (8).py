from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split())) * m
for c in sorted(set(combinations(arr, m))): print(' '.join(map(str, c)))