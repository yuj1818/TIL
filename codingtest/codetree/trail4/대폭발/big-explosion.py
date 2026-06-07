d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)]
grid[r - 1][c - 1] = 1
s = [(r - 1, c - 1)]
t = 1
while t <= m:
    ns = s[:]
    for y, x in s:
        c = 2 ** (t - 1)
        for dy, dx in d:
            ny, nx = y + (dy * c), x + (dx * c)
            if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx]: continue
            ns.append((ny, nx))
            grid[ny][nx] = 1
    s = ns
    t += 1
ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]: ans += 1
print(ans)