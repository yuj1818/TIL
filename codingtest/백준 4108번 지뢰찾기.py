import sys
input = sys.stdin.readline
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
while 1:
    r, c = map(int, input().split())
    if r + c == 0: break
    board = [input().strip() for _ in range(r)]
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                res[i][j] = '*'
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != '*': res[ni][nj] += 1
    for row in res: print(''.join(map(str, row)))