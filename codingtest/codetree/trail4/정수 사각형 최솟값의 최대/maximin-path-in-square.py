n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [row[:] for row in grid]
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0], grid[i][0])
for j in range(1, n):
    dp[0][j] = min(dp[0][j - 1], grid[0][j])
for i in range(1, n):
    for j in range(1, n):
        mv = max(dp[i - 1][j], dp[i][j - 1])
        dp[i][j] = min(mv, dp[i][j])
print(dp[-1][-1])