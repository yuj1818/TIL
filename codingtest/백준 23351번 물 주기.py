from heapq import heappush, heappop
import sys
n, k, a, b = map(int, sys.stdin.readline().split())
p = [k] * n
d = 0
while p.count(0) < 1:
    d += 1
    values = [heappop(p) for _ in range(a)]
    for v in values: heappush(p, v + b)
    p = [x - 1 for x in p]
print(d)
