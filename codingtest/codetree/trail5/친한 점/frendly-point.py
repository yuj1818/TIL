from sortedcontainers import SortedSet
n, m = map(int, input().split())
points = SortedSet([tuple(map(int, input().split())) for _ in range(n)])
for _ in range(m):
    idx = points.bisect_left(tuple(map(int, input().split())))
    if idx == n: print(-1, -1)
    else: print(*points[idx])