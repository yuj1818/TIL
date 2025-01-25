import sys
input = sys.stdin.readline
board = [list(map(int, input().rstrip())) for _ in range(9)]
row = [0] * 9
col = [0] * 9
grid = [0] * 9
zero = []

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            v = 1 << (board[i][j] - 1)
            row[i] |= v
            col[j] |= v
            grid[i // 3 * 3 + j // 3] |= v
        else:
            zero.append((i, j))

def check(b):
    com = 0b111111111
    return com & ~b

def dfs(d):
    if d == len(zero):
        for x in board:
            print(*x, sep='')
        exit()

    r, c = zero[d]
    s = check(row[r] | col[c] | grid[r // 3 * 3 + c // 3])
    for n in range(1, 10):
        if s & (1 << (n - 1)):
            board[r][c] = n
            v = 1 << (n - 1)
            row[r] |= v
            col[c] |= v
            grid[r // 3 * 3 + c // 3] |= v
            dfs(d + 1)
            board[r][c] = 0
            row[r] &= ~v
            col[c] &= ~v
            grid[r // 3 * 3 + c // 3] &= ~v

dfs(0)