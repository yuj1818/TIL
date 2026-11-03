from heapq import heappush, heappop
n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    if x != 0: heappush(hq, -x)
    else:
        if hq: print(-heappop(hq))
        else: print(0)