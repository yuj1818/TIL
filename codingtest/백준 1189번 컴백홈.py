import sys

def dfs(y, x, cnt):
    global ans
    if cnt > k: return
    if y == 0 and x == c - 1:
        if cnt == k: ans += 1
        return
    visited[y][x] = 1
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'T' and not visited[ny][nx]:
            dfs(ny, nx, cnt + 1)
    visited[y][x] = 0

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c, k = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
ans = 0
dfs(r - 1, 0, 1)
print(str(ans))