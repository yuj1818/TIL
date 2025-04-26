import sys
input = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
n = int(input())
board = [[0] * 101 for _ in range(101)]
ans = 0
my, mx = 0, 0
for _ in range(n):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    my, mx = max(my, y), max(mx, x)
    move = [d]
    for _ in range(g):
        for i in range(len(move) - 1, -1, -1): move.append((move[i] + 1) % 4)
    for d in move:
        y, x = y + dy[d], x + dx[d]
        my, mx = max(my, y), max(mx, x)
        if not (0 <= y < 101 and 0 <= x < 101): continue
        board[y][x] = 1

for i in range(my):
    for j in range(mx):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]: ans += 1
print(ans)