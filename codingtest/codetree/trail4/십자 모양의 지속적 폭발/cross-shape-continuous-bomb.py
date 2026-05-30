def bomb(j):
    for i in range(n):
        if grid[i][j] == 0: continue
        for dy, dx in d:
            y, x = i, j
            for _ in range(grid[i][j] - 1):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < n and 0 <= nx < n): break
                grid[ny][nx] = 0
                y, x = ny, nx
        grid[i][j] = 0
        break

def gravity():
    n_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                n_grid[idx][j] = grid[i][j]
                idx -= 1
    return n_grid


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x = int(input()) - 1
    bomb(x)
    grid = gravity()
for row in grid:
    print(' '.join(map(str, row)))