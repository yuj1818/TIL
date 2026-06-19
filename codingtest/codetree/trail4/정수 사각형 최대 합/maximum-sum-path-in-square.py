n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
print(dp[-1][-1])