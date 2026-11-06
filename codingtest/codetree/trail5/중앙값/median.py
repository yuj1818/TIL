from heapq import heappush, heappop
for _ in range(int(input())):
    m = int(input())
    a = list(map(int, input().split()))
    max_hq = []
    min_hq = []
    res = []
    for i in range(m):
        x = a[i]
        if not max_hq or x <= -max_hq[0]:
            heappush(max_hq, -x)
        else:
            heappush(min_hq, x)
        
        if len(max_hq) > len(min_hq) + 1:
            heappush(min_hq, -heappop(max_hq))
        elif len(min_hq) > len(max_hq):
            heappush(max_hq, -heappop(min_hq))

        if i % 2 == 0:
            res.append(-max_hq[0])

    print(*res)        