MIN = -float('inf')
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [[[MIN] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1])
        dp[i][j][1] = max(dp[i - 1][j - 1][0], dp[i - 1][j][1]) + arr[i]
print(max(dp[n][m]))