from collections import Counter
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
for _ in range(t):
    n_marbles = list()
    for y, x in marbles:
        my, mx = -1, -1
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n): continue
            if my == -1: my, mx = ny, nx
            else:
                if grid[ny][nx] > grid[my][mx]: my, mx = ny, nx
        n_marbles.append((my, mx))
    marbles = [x for x, cnt in Counter(n_marbles).items() if cnt == 1]
print(len(marbles))