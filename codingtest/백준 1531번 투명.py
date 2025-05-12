import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            board[y][x] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > m: cnt += 1
print(cnt)