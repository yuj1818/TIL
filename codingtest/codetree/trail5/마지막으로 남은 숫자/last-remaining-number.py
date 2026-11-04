from heapq import heappush, heappop
n = int(input())
hq = []
for x in map(int, input().split()):
    heappush(hq, -x)
while len(hq) >= 2:
    a, b = heappop(hq), heappop(hq)
    if a - b == 0: continue
    heappush(hq, -abs(a - b))
if hq: print(-hq[0])
else: print(-1)