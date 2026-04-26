from itertools import combinations
from collections import deque

def count(cities):
    q = deque(cities)
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for y, x in cities:
        visited[y][x] = 1
        cnt += 1
    while q:
        y, x = q.popleft()
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or not u <= abs(grid[ny][nx] - grid[y][x]) <= d or visited[ny][nx]: continue
            cnt += 1
            q.append((ny, nx))
            visited[ny][nx] = 1
    return cnt

dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for comb in combinations([(i, j) for i in range(n) for j in range(n)], k):
    ans = max(ans, count(comb))
print(ans)
