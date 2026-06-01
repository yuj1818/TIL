def gravity(grid):
    n_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]: 
                n_grid[idx][j] = grid[i][j]
                idx -= 1
    return n_grid

def bomb(sy, sx):
    n_grid = [row[:] for row in grid]
    v = grid[sy][sx] - 1
    n_grid[sy][sx] = 0
    for dy, dx in d:
        y, x = sy, sx
        for _ in range(v):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n): break
            n_grid[ny][nx] = 0
            y, x = ny, nx
    return gravity(n_grid)

def count(grid):
    cnt = 0
    for i in range(n):
        for j in range(1, n):
            if grid[i][j] == 0: continue
            if grid[i][j] == grid[i][j - 1]: cnt += 1
    for j in range(n):
        for i in range(1, n):
            if grid[i][j] == 0: continue
            if grid[i][j] == grid[i - 1][j]: cnt += 1
    return cnt

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        res = bomb(i, j)
        ans = max(ans, count(res))
print(ans)