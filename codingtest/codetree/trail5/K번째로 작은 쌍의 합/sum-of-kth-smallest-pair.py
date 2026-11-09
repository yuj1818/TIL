from heapq import heappush, heappop
n, m, k = map(int, input().split())
arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()))
hq = []
for i in range(n):
    heappush(hq, (arr1[i] + arr2[0], i, 0))
for i in range(k - 1):
    _, i1, i2 = heappop(hq)
    i2 += 1
    if i2 < m:
        heappush(hq, (arr1[i1] + arr2[i2], i1, i2))
ans, _, _ = heappop(hq)
print(ans)