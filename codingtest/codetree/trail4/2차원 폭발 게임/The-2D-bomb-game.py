def gravity(grid):
    n_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                n_grid[idx][j] = grid[i][j]
                idx -= 1
    return n_grid

def bomb():
    isExploded = False
    n_grid = [row[:] for row in grid]
    for j in range(n):
        tmp = [0]
        for i in range(1, n):
            if grid[tmp[-1]][j] == 0:
                tmp = [i]
                continue
            if grid[tmp[-1]][j] == grid[i][j]:
                tmp.append(i)
            else:
                if len(tmp) >= m and grid[tmp[-1]][j] != 0:
                    isExploded = True
                    for x in tmp: n_grid[x][j] = 0
                tmp = [i]
        if tmp and grid[tmp[-1]][j] != 0 and len(tmp) >= m:
            isExploded = True
            for x in tmp: n_grid[x][j] = 0
    return gravity(n_grid), isExploded

def rotate():
    n_grid = []
    for j in range(n):
        n_grid.append([])
        for i in range(n - 1, -1, -1):
            n_grid[-1].append(grid[i][j])
    return gravity(n_grid)

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for t in range(k + 1):
    isExploded = True
    while isExploded:
        isExploded = False
        grid, isExploded = bomb()
    if t == k: break
    grid = rotate()
ans = 0
for j in range(n):
    for i in range(n - 1, -1, -1):
        if grid[i][j] == 0: break
        ans += 1
print(ans)