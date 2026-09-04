d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(n)]
sy, sx = points[0]
visited[sy][sx] = 1
ans = 0

def dfs(y, x, cnt):
    global ans
    if y == points[cnt][0] and x == points[cnt][1]:
        cnt += 1
        if cnt == m:
            ans += 1
            return
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] or visited[ny][nx]: continue
        visited[ny][nx] = 1
        dfs(ny, nx, cnt)
        visited[ny][nx] = 0

dfs(sy, sx, 1)
print(ans)
