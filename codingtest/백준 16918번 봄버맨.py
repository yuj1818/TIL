import sys
input = sys.stdin.readline

def bomb(board):
    nboard = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                nboard[i][j] = '.'
                for dy, dx in d:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < r and 0 <= nx < c:
                        nboard[ny][nx] = '.'
    return nboard

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
ans = []
if n == 1:
    ans = board
elif n % 2 == 0:
    ans = [['O'] * c for _ in range(r)]
elif n % 4 == 3:
    ans = bomb(board)
else:
    ans = bomb(bomb(board))
for i in range(r):
    print(''.join(ans[i]))