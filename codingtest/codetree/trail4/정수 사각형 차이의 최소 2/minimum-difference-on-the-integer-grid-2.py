n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[[float('inf')] * 101 for _ in range(n)] for _ in range(n)]
dp[0][0][grid[0][0]] = grid[0][0]
for i in range(n):
    for j in range(n):
        for k in range(1, 101):
            min_k = min(k, grid[i][j])
            dp[i][j][min_k] = min(dp[i][j][min_k], max(grid[i][j], min(dp[i - 1][j][k], dp[i][j - 1][k])))
ans = float('inf')
for k in range(1, 101):
    if dp[-1][-1][k] != float('inf'):
        ans = min(ans, dp[-1][-1][k] - k)
print(ans)