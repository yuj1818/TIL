n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n * 2)]
dp = [[-1] * (n + 1) for _ in range(n * 2 + 1)]
dp[0][0] = 0
for i in range(1, n * 2 + 1):
    for j in range(min(i + 1, n + 1)):
        if j > 0:
            dp[i][j] = max(dp[i - 1][j - 1] + arr[i][0], dp[i][j])
        if i > j:
            dp[i][j] = max(dp[i - 1][j] + arr[i][1], dp[i][j])
print(dp[2 * n][n])