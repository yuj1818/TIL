import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
pos = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
ans = 0
visited = [[0] * n for _ in range(n)]

def dfs(y, x, tidx):
    global ans
    if [y, x] == pos[tidx]:
        if tidx == m - 1:
            ans += 1
            return
        else: tidx += 1
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and not road[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny, nx, tidx)
            visited[ny][nx] = 0

sy, sx = pos[0]
visited[sy][sx] = 1
dfs(sy, sx, 0)
print(ans)