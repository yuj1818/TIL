import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
if M == 0:
    print(0)
    sys.exit()
board = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d, z]

def posNxt(i, j, d, s):
    if d == 1 or d == 2:
        if d == 1: s += (R - 1) * 2 - i
        else: s += i
        s %= (R - 1) * 2
        if s < R: return dr[s], j, 2
        else: return dr[s], j, 1
    else:
        if d == 3: s += j
        else: s += (C - 1) * 2 - j
        s %= (C - 1) * 2
        if s < C: return i, dc[s], 3
        else: return i, dc[s], 4

def move(board):
    nboard = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0: continue
            s, d, z = board[i][j]
            ni, nj, nd = posNxt(i, j, d, s)
            if nboard[ni][nj] == 0 or nboard[ni][nj][-1] < z:
                nboard[ni][nj] = (s, nd, z)
    return nboard

pi = 0
total = 0
dr = [i for i in range(R)] + [i for i in range(R - 2, 0, -1)]
dc = [j for j in range(C)] + [j for j in range(C - 2, 0, -1)]
while pi < C:
    for r in range(R):
        if board[r][pi]:
            total += board[r][pi][-1]
            board[r][pi] = 0
            break
    board = move(board)
    pi += 1
print(total)