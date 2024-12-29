from itertools import combinations
import sys
while 1:
    k, *s = map(int, sys.stdin.readline().split())
    if k == 0: break
    for comb in combinations(s, 6):
        print(*comb)
    print()