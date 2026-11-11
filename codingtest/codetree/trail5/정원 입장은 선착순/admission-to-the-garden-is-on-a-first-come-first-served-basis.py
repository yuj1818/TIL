from heapq import heappush, heappop
n = int(input())
arr = []
for i in range(n):
    a, t = map(int, input().split())
    arr.append((a, i + 1, t))
arr.append((float('inf'), n + 1, 0))
arr.sort()
et, ans = 0, 0
hq = []
for a, i, t in arr:
    while a >= et and hq:
        ci, ca, ct = heappop(hq)
        ans = max(ans, et - ca)
        et += ct
    if a >= et:
        et = a + t
    else:
        heappush(hq, (i, a, t))
print(ans)