def escape(y, x):
    global ans
    if ans: return
    if y == n - 1 and x == m - 1:
        ans = 1
        return
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < m) or not grid[ny][nx] or visited[ny][nx]: continue
        visited[ny][nx] = 1
        escape(ny, nx)

d = [(0, 1), (1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
q = [(0, 0)]
ans = 0
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
escape(0, 0)
print(ans)
