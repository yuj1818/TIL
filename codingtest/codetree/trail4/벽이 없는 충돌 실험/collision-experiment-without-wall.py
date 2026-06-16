MAX_SIZE = 4001
T = int(input())
dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d_map = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
for _ in range(T):
    N = int(input())
    marbles = [[] for _ in range(N)]
    for i in range(N):
        x, y, w, d = input().split()
        x, y, w = int(x), int(y), int(w)
        marbles[i] = (2 * y + 2000, 2 * x + 2000, w, d_map[d])
    t = 0
    ans = -1
    for t in range(1, MAX_SIZE + 1):
        for i in range(N):
            if not marbles[i]: continue
            y, x, w, d = marbles[i]
            dy, dx = dyx[d]
            ny, nx = y + dy, x + dx
            if not (0 <= ny < MAX_SIZE and 0 <= nx < MAX_SIZE):
                marbles[i] = 0
                continue
            marbles[i] = (ny, nx, w, d)
        counter = dict()
        for i in range(N):
            if not marbles[i]: continue
            y, x, w, d = marbles[i]
            if (y, x) in counter:
                cw, ci = counter[(y, x)]
                if cw < w:
                    marbles[ci] = 0
                    counter[(y, x)] = (w, i)
                elif cw == w and ci < i:
                    marbles[ci] = 0
                    counter[(y, x)] = (w, i)
                else:
                    marbles[i] = 0
                ans = t
            else: counter[(y, x)] = (w, i)
    print(ans)