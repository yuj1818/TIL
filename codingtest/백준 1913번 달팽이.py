import sys
def main():
    n = int(sys.stdin.readline())
    t = int(sys.stdin.readline())
    r, c, i, j = 0, 0, 0, 0
    s = n ** 2
    board = [[0] * n for _ in range(n)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    di = 0
    while s > 0:
        if s == t:
            r, c = i + 1, j + 1
        board[i][j] = s
        ni, nj = i + d[di][0], j + d[di][1]
        if ni < 0 or ni >= n or nj < 0 or nj >= n or board[ni][nj]:
            di = (di + 1) % 4
            ni, nj = i + d[di][0], j + d[di][1]
        i, j = ni, nj
        s -= 1
    for i in range(n):
        sys.stdout.write(' '.join(map(str, board[i])) + '\n')
    sys.stdout.write(f'{r} {c}')
main()