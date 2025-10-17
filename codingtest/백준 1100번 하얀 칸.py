import sys
input = sys.stdin.readline
board = [input().strip() for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'F':
            if (i % 2 and j % 2) or (not i % 2 and not j % 2): ans += 1
print(ans)