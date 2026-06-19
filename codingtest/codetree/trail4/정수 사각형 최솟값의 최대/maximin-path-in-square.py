n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mv = max(dp[i - 1][j], dp[i][j - 1])
        if mv == 0: mv = 1000000
        dp[i][j] = min(mv, grid[i][j])
print(dp[-1][-1])