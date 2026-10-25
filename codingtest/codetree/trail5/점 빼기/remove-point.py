from sortedcontainers import SortedSet
n, m = map(int, input().split())
points = SortedSet([tuple(map(int, input().split())) for _ in range(n)])
for _ in range(m):
    k = int(input())
    idx = points.bisect_left((k, -float('inf')))
    if idx == len(points):
        print('-1 -1');
        continue
    print(*points[idx])
    points.remove(points[idx])