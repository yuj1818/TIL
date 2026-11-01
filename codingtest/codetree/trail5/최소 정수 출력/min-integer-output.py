from heapq import heappush, heappop
n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not hq: print(0)
        else: print(heappop(hq))
    else: heappush(hq, x)