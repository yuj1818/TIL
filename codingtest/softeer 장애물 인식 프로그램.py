import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(y, x):
    global cnt
    cnt += 1
    visited[y][x] = 1
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= nx < n and 0 <= ny < n and board[ny][nx] and not visited[ny][nx]:
            dfs(ny, nx)

ans = []
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)
print(len(ans))
ans.sort()
print(*ans, sep='\n')