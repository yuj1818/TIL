from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(r, c, d):
    q = deque([(r, c, d, k)])
    for i in range(k + 1): visited[r][c][i] = 1
    while q:
        y, x, d, t = q.popleft()
        if y == n - 1 and x == m - 1: return d
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not board[ny][nx] and not visited[ny][nx][t]:
                    q.append((ny, nx, d + 1, t))
                    visited[ny][nx][t] = 1
                elif t > 0 and board[ny][nx] and not visited[ny][nx][t - 1]:
                    q.append((ny, nx, d + 1, t - 1))
                    visited[ny][nx][t - 1] = 1
    return -1

print(bfs(0, 0, 1))