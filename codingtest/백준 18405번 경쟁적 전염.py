import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
if s == 0 or board[x - 1][y - 1] != 0:
    print(board[x - 1][y - 1])
    sys.exit()
board[x - 1][y - 1] = -1
arr = [(x - 1, y - 1)]
for _ in range(s):
    narr = []
    num = 0
    while arr:
        y, x = arr.pop()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] < 0: continue
                if board[ny][nx] > 0 and (num <= 0 or board[ny][nx] < num):
                    num = board[ny][nx]
                board[ny][nx] = -1
                narr.append((ny, nx))
    arr = narr
    if num > 0:
        print(num)
        sys.exit()
print(0)