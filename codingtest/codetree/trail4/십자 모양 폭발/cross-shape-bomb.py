def bomb(y, x):
    v = grid[y][x] - 1
    grid[y][x] = 0
    for dy, dx in d:
        cy, cx = y, x
        for _ in range(v):
            cy += dy
            cx += dx
            if not (0 <= cy < n and 0 <= cx < n): break
            grid[cy][cx] = 0

def gravity():
    n_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                n_grid[idx][j] = grid[i][j]
                idx -= 1
    return n_grid

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
bomb(r - 1, c - 1)
grid = gravity()
for row in grid:
    print(' '.join(map(str, row)))