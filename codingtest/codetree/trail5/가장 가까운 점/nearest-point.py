from heapq import heappush, heappop
n, m = map(int, input().split())
hq = []
for _ in range(n):
    x, y = map(int, input().split())
    heappush(hq, (x + y, x, y))
for _ in range(m):
    l, x, y = heappop(hq)
    heappush(hq, (l + 4, x + 2, y + 2))
_, x, y = heappop(hq)
print(x, y)