n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        for y in range(i):
            for x in range(j):
                if dp[y][x] == -1: continue
                if grid[y][x] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[y][x] + 1)
ans = 0
for i in range(n):
    for j in range(m):
        if ans < dp[i][j]: ans = dp[i][j]
print(ans)