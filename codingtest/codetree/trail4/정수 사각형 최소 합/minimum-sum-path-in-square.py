n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    for j in range(n - 1, -1, -1):
        mv = min(dp[i - 1][j], dp[i][(j + 1) % n])
        if mv == float('inf'): mv = 0
        dp[i][j] = mv + grid[i][j]
print(dp[-1][0])