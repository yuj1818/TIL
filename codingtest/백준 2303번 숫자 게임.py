from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
mv, mi = 0, -1
for i in range(n):
    a = list(map(int, input().split()))
    for comb in combinations(a, 3):
        v = sum(comb) % 10
        if v >= mv:
            mv = v
            mi = i
print(mi + 1)