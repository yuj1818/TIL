from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x):
    global cnt
    cur = 1
    q = deque([(y, x)])
    visited[y][x] = year
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] != year:
                if board[ny][nx]:
                    cur += 1
                    q.append((ny, nx))
                    visited[ny][nx] = year
                elif board[y][x]:
                    board[y][x] -= 1
                    if not board[y][x]:
                        cnt -= 1
                        cur -= 1
    return cnt == cur

def check():
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if board[i][j]: return bfs(i, j)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            cnt += 1

isDiv = False
year = 0
visited = [[0] * m for _ in range(n)]

while cnt:
    year += 1
    if not check():
        isDiv = True
        break

print(year - 1 if isDiv else 0)