from collections import deque
import sys
input = sys.stdin.readline
d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

def bfs(cy, cx, gy, gx):
    visited = [[0] * n for _ in range(n)]
    visited[cy][cx] = 1
    q = deque([(cy, cx, 0)])
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (gy, gx): return cnt
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                q.append((ny, nx, cnt + 1))
                visited[ny][nx] = 1
    return 0

for _ in range(int(input())):
    n = int(input())
    cy, cx = map(int, input().split())
    gy, gx = map(int, input().split())
    print(bfs(cy, cx, gy, gx))