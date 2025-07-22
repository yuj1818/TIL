from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    q = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1
    while q:
        y, x, t, d = q.popleft()
        if y == n - 1 and x == m - 1: return d
        isDay = d % 2
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not board[ny][nx] and not visited[ny][nx][t]:
                    visited[ny][nx][t] = d
                    q.append((ny, nx, t, d + 1))
                elif board[ny][nx] == 1 and t < k and not visited[ny][nx][t + 1]:
                    if isDay:
                        visited[ny][nx][t + 1] = d
                        q.append((ny, nx, t + 1, d + 1))
                    else: q.append((y, x, t, d + 1))
    return -1

print(bfs())