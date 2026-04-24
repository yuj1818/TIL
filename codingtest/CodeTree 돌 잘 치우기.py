from collections import deque
from itertools import combinations

def count(grid):
    q = deque()
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for y, x in pos:
        q.append((y, x))
        visited[y][x] = 1
        cnt += 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] or visited[ny][nx]: continue
            q.append((ny, nx))
            visited[ny][nx] = 1
            cnt +=1
    return cnt

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pos = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j]: stones.append((i, j))
sn = len(stones)
ans = 0
q = deque()
visited = [[0] * n for _ in range(n)]
for comb in combinations(stones, m):
    n_grid = [x[:] for x in grid]
    for y, x in comb: n_grid[y][x] = 0
    ans = max(ans, count(n_grid))
print(ans)
