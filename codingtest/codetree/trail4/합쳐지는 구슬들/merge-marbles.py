def move(y, x, idx, di, w):
    dy, dx = dyx[di]
    ny, nx = y + dy, x + dx
    if not (0 <= ny < N and 0 <= nx < N):
        di = (di + 2) % 4
        ny, nx = y, x
    if (ny, nx) not in n_marbles:
        n_marbles[(ny, nx)] = (idx, di, w)
    else:
        cidx, cdi, cw = n_marbles[(ny, nx)]
        if cidx > idx: n_marbles[(ny, nx)] = (cidx, cdi, cw + w)
        else: n_marbles[(ny, nx)] = (idx, di, cw + w)

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d_map = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
N, M, T = map(int, input().split())
marbles = dict()
for i in range(M):
    r, c, d, w = input().split()
    r, c, w = int(r) - 1, int(c) - 1, int(w)
    marbles[(r, c)] = (i, d_map[d], w)
for _ in range(T):
    n_marbles = dict()
    for y, x in marbles:
        idx, di, w = marbles[(y, x)]
        move(y, x, idx, di, w)
    marbles = n_marbles
print(len(marbles), end=' ')
print(sorted(marbles.values(), key=lambda x: x[-1])[-1][-1])