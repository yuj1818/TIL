import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(y, x, dy, dx):
    cnt = 0
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs(ry, rx, by, bx):
    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[ry][rx][by][bx] = 1
    q = [(ry, rx, by, bx, 1)]
    while q:
        ry, rx, by, bx, cnt = q.pop(0)
        if cnt > 10: return -1
        for dy, dx in d:
            nry, nrx, rcnt = move(ry, rx, dy, dx)
            nby, nbx, bcnt = move(by, bx, dy, dx)
            if board[nby][nbx] == 'O': continue
            if board[nry][nrx] == 'O': return cnt
            if (nry, nrx) == (nby, nbx):
                if rcnt > bcnt:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx
            if visited[nry][nrx][nby][nbx]: continue
            q.append((nry, nrx, nby, nbx, cnt + 1))
            visited[nry][nrx][nby][nbx] = 1
    return -1

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
ry, rx, by, bx = 0, 0, 0, 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'B': by, bx = i, j
        elif board[i][j] == 'R': ry, rx = i, j
print(bfs(ry, rx, by, bx))