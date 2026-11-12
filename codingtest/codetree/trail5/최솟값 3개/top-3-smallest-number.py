from heapq import heappush, heappop
n = int(input())
hq = []
for x in map(int, input().split()):
    heappush(hq, x)
    if len(hq) < 3:
        print(-1)
        continue
    res = 1
    tmp = []
    for _ in range(3):
        t = heappop(hq)
        tmp.append(t)
        res *= t
    for t in tmp:
        heappush(hq, t)
    print(res)
