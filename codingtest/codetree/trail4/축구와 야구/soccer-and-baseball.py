n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
arr.sort()
dp = [[[0] * 10 for _ in range(12)] for _ in range(n + 1)]
dp[0][0][0] = 0
for i in range(1, n + 1):
    for j in range(min(i + 1, 12)):
        for k in range(min(i + 1, 10)):
            dp[i][j][k] = dp[i - 1][j][k]
            if j > 0:
                dp[i][j][k] = max(dp[i - 1][j - 1][k] + arr[i][0], dp[i][j][k])
            if k > 0:
                dp[i][j][k] = max(dp[i - 1][j][k - 1] + arr[i][1], dp[i][j][k])
print(dp[n][11][9])