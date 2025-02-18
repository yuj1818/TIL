from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
zero = []
for i in range(n):
    for j in range(m):
        if not board[i][j]: zero.append((i, j))
        elif board[i][j] == 2: virus.append((i, j))

ans = 0
lz = len(zero)
for i in range(lz):
    board[zero[i][0]][zero[i][1]] = 1
    for j in range(i + 1, lz):
        board[zero[j][0]][zero[j][1]] = 1
        for k in range(j + 1, lz):
            board[zero[k][0]][zero[k][1]] = 1
            q = deque(virus)
            cboard = [board[i][::] for i in range(n)]
            while q:
                y, x = q.popleft()
                for dy, dx in d:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < m and not cboard[ny][nx]:
                        q.append((ny, nx))
                        cboard[ny][nx] = 2
            cnt = 0
            for a in range(n):
                for b in range(m):
                    if not cboard[a][b]: cnt += 1
            if ans < cnt: ans = cnt
            board[zero[k][0]][zero[k][1]] = 0
        board[zero[j][0]][zero[j][1]] = 0
    board[zero[i][0]][zero[i][1]] = 0

print(ans)