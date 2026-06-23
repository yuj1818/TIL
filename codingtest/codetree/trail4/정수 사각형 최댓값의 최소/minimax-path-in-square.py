n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1000000] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mv = min(dp[i - 1][j], dp[i][j - 1])
        if mv == 1000000: mv = 0
        dp[i][j] = max(mv, grid[i][j])
print(dp[-1][-1])