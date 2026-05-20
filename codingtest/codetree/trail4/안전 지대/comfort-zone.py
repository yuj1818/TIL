import sys
input = sys.stdin.readline

def bfs(i, j):
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m) or grid[ny][nx] <= k or visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
mk = max(map(max, grid))
ak, ac = mk, 0
for k in range(1, mk):
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    if ac < cnt:
        ak, ac = k, cnt
print(ak, ac)