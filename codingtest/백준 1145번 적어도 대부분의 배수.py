from math import lcm
from itertools import combinations
ans = float('inf')
for c in combinations(map(int, input().split()), 3):
    ans = min(ans, lcm(*c))
print(ans)