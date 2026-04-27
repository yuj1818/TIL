def reverse(y, x, grid):
    for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < m): continue
        grid[ny][nx] = grid[ny][nx] ^ 1

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dyx = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
ans = float('inf')
for i in range(1 << m):
    n_grid = [x[:] for x in grid]
    tmp = 0
    for j in range(m):
        if i & (1 << j):
            reverse(0, j, n_grid)
            tmp += 1
    for r in range(1, n):
        for c in range(m):
            if n_grid[r - 1][c] == 0:
                reverse(r, c, n_grid)
                tmp += 1
    sig = 1
    for r in range(n):
        for c in range(m):
            if n_grid[r][c] == 0:
                sig = 0
                break
    if sig: ans = min(ans, tmp)

if ans == float('inf'): print(-1)
else: print(ans)
