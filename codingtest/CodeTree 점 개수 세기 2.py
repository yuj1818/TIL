from bisect import bisect_left, bisect_right
from sortedcontainers import SortedSet

n, q = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]
pos = SortedSet()
for p in points: pos.update(p)
pm = dict()
for i, x in enumerate(pos): pm[x] = i + 1
acc = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
for y, x in points:
    ny, nx = pm[y], pm[x]
    acc[ny][nx] = 1
for i in range(1, len(pos) + 1):
    for j in range(1, len(pos) + 1):
        acc[i][j] += acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1]

for y1, x1, y2, x2 in queries:
    ny1 = bisect_left(pos, y1) + 1
    nx1 = bisect_left(pos, x1) + 1
    ny2 = bisect_right(pos, y2)
    nx2 = bisect_right(pos, x2)
    print(acc[ny2][nx2] - acc[ny2][nx1 - 1] - acc[ny1 - 1][nx2] + acc[ny1 - 1][nx1 - 1])
