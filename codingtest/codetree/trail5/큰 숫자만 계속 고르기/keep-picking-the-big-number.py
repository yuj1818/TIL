from heapq import heappush, heappop
n, m = map(int, input().split())
hq = []
for x in map(int, input().split()):
    heappush(hq, -x)
for _ in range(m):
    heappush(hq, heappop(hq) + 1)
print(-heappop(hq))