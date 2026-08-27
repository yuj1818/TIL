from sortedcontainers import SortedSet
n, m = map(int, input().split())
a = SortedSet(map(int, input().split()))
for _ in range(m):
    x = int(input())
    idx = a.bisect_left(x)
    if idx == n: print(-1)
    else: print(a[idx])