import sys
input = sys.stdin.readline
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ratio = [{(-2, 0): 0.02, (-1, -1): 0.1, (-1, 0): 0.07, (-1, 1): 0.01, (0, -2): 0.05, (1, -1): 0.1, (1, 0): 0.07, (1, 1): 0.01, (2, 0): 0.02},
          {(0, -2): 0.02, (1, -1): 0.1, (0, -1): 0.07, (-1, -1): 0.01, (2, 0): 0.05, (1, 1): 0.1, (0, 1): 0.07, (-1, 1): 0.01, (0, 2): 0.02},
          {(2, 0): 0.02, (1, 1): 0.1, (1, 0): 0.07, (1, -1): 0.01, (0, 2): 0.05, (-1, 1): 0.1, (-1, 0): 0.07, (-1, -1): 0.01, (-2, 0): 0.02},
          {(0, 2): 0.02, (-1, 1): 0.1, (0, 1): 0.07, (1, 1): 0.01, (-2, 0): 0.05, (-1, -1): 0.1, (0, -1): 0.07, (1, -1): 0.01, (0, -2): 0.02}]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sand, di, cnt, lim = 0, 0, 0, 1
sy, sx = n // 2, n // 2
while sy + sx > 0:
    dy, dx = d[di]
    for r in range(lim):
        sy, sx = sy + dy, sx + dx
        ns = board[sy][sx]
        for k, v in ratio[di].items():
            py, px = k
            nny, nnx = sy + py, sx + px
            ms = int(board[sy][sx] * v)
            if 0 <= nny < n and 0 <= nnx < n: board[nny][nnx] += ms
            else: sand += ms
            ns -= ms
        ay, ax = sy + dy, sx + dx
        if 0 <= ay < n and 0 <= ax < n: board[ay][ax] += ns
        else: sand += ns
        board[sy][sx] = 0
        if sy + sx == 0: break
    cnt += 1
    if cnt == 2:
        cnt = 0
        lim += 1
    di = (di + 1) % 4
print(sand)