n = int(input())
dp = [[1] * n for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
grid = [list(map(int, input().split())) for _ in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        arr.append((grid[i][j], i, j))
arr.sort()
for v, y, x in arr:
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] <= v: continue
        dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1)
ans = 1
for i in range(n):
    for j in range(n):
        if ans < dp[i][j]: ans = dp[i][j]
print(ans)