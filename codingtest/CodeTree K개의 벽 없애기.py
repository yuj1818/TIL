from itertools import combinations
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
tr = lambda x: int(x) - 1
n, k = map(int, input().split())
grid = []
walls = []
ans = float('inf')
for i in range(n):
    r = list(map(int, input().split()))
    for j in range(n):
        if r[j]: walls.append((i, j))
    grid.append(r)
sy, sx = map(tr, map(int, input().split()))
ey, ex = map(tr, map(int, input().split()))
for wall in combinations(walls, k):
    n_grid = [r[:] for r in grid]
    for i, j in wall: n_grid[i][j] = 0
    q = [(sy, sx, 0)]
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1
    while q:
        y, x, cnt = q.pop(0)
        if y == ey and x == ex:
            if ans > cnt: ans = cnt
            break
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or n_grid[ny][nx] or visited[ny][nx]: continue
            q.append((ny, nx, cnt + 1))
            visited[ny][nx] = 1
if ans == float('inf'): print(-1)
else: print(ans)
