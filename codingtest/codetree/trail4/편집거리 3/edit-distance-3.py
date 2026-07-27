MAX = float('inf')
a, b = input(), input()
n, m = len(a), len(b)
dp = [[MAX] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n + 1):
    for j in range(m + 1):
        if i == 0: dp[i][j] = j
        elif j == 0: dp[i][j] = i
        else:
            if a[i - 1] == b[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1, dp[i - 1][j] + 1)
print(dp[-1][-1])