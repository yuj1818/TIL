import heapq
n, p = map(int, input().split())
a = list(map(int, input().split()))
hq = []
for i in range(1, n - 1):
    if a[i - 1] > a[i] and a[i + 1] > a[i]:
        heapq.heappush(hq, (a[i], i))
s = 0
for _ in range(p):
    if s >= n: break
    while hq and hq[0][1] < s + 1:
        heapq.heappop(hq)
    if hq:
        v, mi = hq[0]
        if not (a[mi - 1] > a[mi] and a[mi + 1] > a[mi]):
            hq.heappop(hq)
        heapq.heappop(hq)
        a[s], a[mi] = a[mi], a[s]
        affected = {s - 1, s, s + 1, mi - 1, mi, mi + 1}
        for idx in affected:
            if 1 <= idx <= n - 2:
                if a[idx - 1] > a[idx] and a[idx + 1] > a[idx]:
                    heapq.heappush(hq, (a[idx], idx))
    s += 1

print(*a)
