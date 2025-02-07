from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
maze = []
ghost = []
sy, sx, gy, gx = 0, 0, 0, 0
for row in range(n):
    line = input()
    for col in range(m):
        x = line[col]
        if x == 'G':
            ghost.append((row, col))
        elif x == 'N':
            sy, sx = row, col
        elif x == 'D':
            gy, gx = row, col
    maze.append(line)

def bfs(sy, sx):
    visited = [[-1] * m for _ in range(n)]
    q = deque([(sy, sx, 0)])
    visited[sy][sx] = 0
        
    while q:
        y, x, cnt = q.popleft()
        if y == gy and x == gx:
            return cnt
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
                if maze[ny][nx] != '#':
                    q.append((ny, nx, cnt + 1))
                    visited[ny][nx] = cnt + 1
    return -1

ghost_time = min([abs(y - gy) + abs(x - gx) for y, x in ghost] + [n * m])
n_time = bfs(sy, sx)
if n_time < 0 or ghost_time <= n_time:
    print('No')
else:
    print('Yes')