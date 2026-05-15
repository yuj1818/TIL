d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, k = map(int, input().split())
grid = []
rotten = []
ans = [[-2] * n for _ in range(n)]
for i in range(n):
    r = list(map(int, input().split()))
    for j in range(n):
        if r[j] == 2: rotten.append((i, j))
        if r[j] == 0: ans[i][j] = -1
    grid.append(r)
for ry, rx in rotten:
    ans[ry][rx] = 0
    q = [(ry, rx)]
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] == 0 or (ans[ny][nx] > -1 and ans[y][x] + 1 >= ans[ny][nx]): continue
            q.append((ny, nx))
            ans[ny][nx] = ans[y][x] + 1
for r in ans: print(' '.join(map(str, r)))
