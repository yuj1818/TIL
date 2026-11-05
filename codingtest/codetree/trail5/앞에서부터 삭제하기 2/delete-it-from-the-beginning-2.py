from heapq import heappop, heappush, heapify
n = int(input())
a = list(map(int, input().split()))
hq = [(x, i) for i, x in enumerate(a)]
heapify(hq)
removed = set()
total, l = sum(a), n
ans = 0
for i in range(n - 2):
    total -= a[i]
    l -= 1
    removed.add((a[i], i))
    while hq[0] in removed:
        heappop(hq)
    x, _ = hq[0]
    avg = (total - x) / (l - 1)
    ans = max(ans, avg)
print(f'{ans:.2f}')