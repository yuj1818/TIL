from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
for comb in sorted(set(combinations(a, m))):
    print(' '.join(map(str, comb)))
