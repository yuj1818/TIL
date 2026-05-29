d = {'L':(0, -1), 'R': (0,  1), 'U': (-1, 0), 'D': (1, 0)}
grid = [list(map(int, input().split())) for _ in range(4)]
dy, dx = d[input()]
n_grid = [[0] * 4 for _ in range(4)]
for x in range(4):
    sy, sx = abs(x * dx), abs(x * dy)
    s = [(abs(sy + dy * i), abs(sx + dx * i)) for i in range(4)]
    tmp = [grid[y][x] for y, x in s if grid[y][x]]
    if not dx: sy = (3 if dy > 0 else 0)
    if not dy: sx = (3 if dx > 0 else 0)
    tmp = tmp[::(dy or dx)]
    while tmp:
        v = tmp.pop()
        if tmp and v == tmp[-1]:
            tmp.pop()
            n_grid[sy][sx] = v * 2
        else:
            n_grid[sy][sx] = v
        sy, sx = sy + -1 * dy, sx + -1 * dx
for row in n_grid:
    print(' '.join(map(str, row)))
