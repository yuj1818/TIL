n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    sig = 0
    for j in range(k - 1, k + m - 1):
        if grid[i][j] == 1: 
            for x in range(k - 1, k + m - 1):
                grid[i - 1][x] = 1
            sig = 1
            break
    if sig: break
else:
    for j in range(k - 1, k + m - 1):
        grid[-1][j] = 1

for row in grid:
    print(' '.join(map(str, row)))