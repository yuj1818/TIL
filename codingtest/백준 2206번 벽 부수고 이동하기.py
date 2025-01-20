from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(r, c, d):
    q = deque([(r, c, d)])
    visited[r][c][d] = 1
    while q:
        y, x, z = q.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x][z]
        for dy, dx in dyx:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and z == 0:
                    visited[ny][nx][1] = visited[y][x][z] + 1
                    q.append((ny, nx, 1))
                elif board[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((ny, nx, z))
    return -1

print(bfs(0, 0, 0))