import sys
input = sys.stdin.readline

def bfs(y, x):
    q = [(y, x)]
    board[y][x] = '.'
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == '#':
                board[ny][nx] = '.'
                q.append((ny, nx))

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            bfs(i, j)
            ans += 1
print(ans)