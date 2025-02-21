input = open(0).readline
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
trans = lambda x: (int(x[0]), x[1])

def play(board, info, n):
    ct, i, d = 0, 0, 0
    board[0][0] = 1
    s = [(0, 0)]
    while True:
        t, r = info[i]
        dy, dx = dyx[d]
        diff = t - ct
        for x in range(diff):
            ct += 1
            sy, sx = s[-1]
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1:
                if board[ny][nx] == 0:
                    ey, ex = s.pop(0)
                    board[ey][ex] = 0
                board[ny][nx] = 1
                s.append((ny, nx))
            else:
                return ct
        d = ((d - 1) if r == 'L' else (d + 1)) % 4
        i += 1

def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    for _ in range(int(input())):
        y, x = map(int, input().split())
        board[y - 1][x - 1] = 2
    info = [trans(input().strip().split()) for _ in range(int(input()))]
    info.append((info[-1][0] + n + 1, ''))
    print(play(board, info, n))

main()