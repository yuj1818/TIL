from itertools import combinations
from math import gcd
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ans = 0
    n, *a = map(int, input().split())
    for c in combinations(a, 2): ans += gcd(*c)
    print(ans)
