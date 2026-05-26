n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
n_grid = [row[:] for row in grid]
info = list(zip([m1, m2, m3, m4], [(-1, 1), (-1, -1), (1, -1), (1, 1)]))
if dir: info = info[::-1]
r, c = r - 1, c - 1
for m, (dr, dc) in info:
    if dir: dr, dc = -1 * dr, -1 * dc
    for _ in range(m):
        nr, nc = r + dr, c + dc
        n_grid[nr][nc] = grid[r][c]
        r, c = nr, nc
for row in n_grid:
    print(' '.join(map(str, row)))