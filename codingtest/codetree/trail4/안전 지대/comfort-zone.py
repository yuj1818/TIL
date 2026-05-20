import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

def dfs(y, x):
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < m) or grid[ny][nx] <= k or visited[ny][nx]: continue
        visited[ny][nx] = 1
        dfs(ny, nx)

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s = sorted(set(x for row in grid for x in row))
if s[0] - 1 > 0: s = [s[0] - 1] + s
ak, ac = 0, -1
for k in s:
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j)
    if cnt > ac:
        ak, ac = k, cnt
print(ak, ac)