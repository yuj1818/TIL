from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c = map(int, input().split())
board = []
fire = []
sy, sx = 0, 0
for i in range(r):
    row = input().strip()
    for j in range(c):
        if row[j] == 'J':
            sy, sx = i, j
        elif row[j] == 'F':
            fire.append((i, j))
    board.append(row)

def bfs(pos, isFire):
    q = deque()
    visited = [[0] * c for _ in range(r)]
    for i, j in pos:
        q.append((i, j, 1))
        visited[i][j] = 1
    while q:
        y, x, cnt = q.popleft()
        if not isFire and (y == 0 or y == r - 1 or x == 0 or x == c - 1):
            return cnt
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and board[ny][nx] != '#':
                if not isFire and fire_cnt[ny][nx] > 0 and fire_cnt[ny][nx] <= cnt + 1: continue
                q.append((ny, nx, cnt + 1))
                visited[ny][nx] = cnt + 1
    return visited if isFire else -1

fire_cnt = bfs(fire, True)
escape = bfs([(sy, sx)], False)
print(escape if escape >= 0 else 'IMPOSSIBLE')