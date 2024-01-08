import os, io
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
matrix = []
sx, sy = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            sy, sx = i, j
    matrix.append(line)

visited = [[0] * m for _ in range(n)]
cnt_matrix = [[0] * m for _ in range(n)]

visited[sy][sx] = 1
q = deque([(sy, sx)])

while q:
    y, x = q.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and matrix[ny][nx] == 1:
            q.append((ny, nx))
            visited[ny][nx] = 1
            cnt_matrix[ny][nx] = cnt_matrix[y][x] + 1

for i in range(n):
    print(' '.join(['-1' if not visited[i][j] and matrix[i][j] == 1 else str(cnt_matrix[i][j]) for j in range(m)]))