import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
d = [(1, 0), (1, 0), (-1, 0), (-1, 0)]

def dfs(y, x):
    global sig
    if y == n - 1: sig = True
    if sig: return
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and not board[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny, nx)


m, n = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
sig = False
for j in range(n):
    for i in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j)
        if sig: break
    if sig: break
print('YES' if sig else 'NO')