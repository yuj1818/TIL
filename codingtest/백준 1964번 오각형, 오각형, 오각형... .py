n = int(input())
dp = [0] * (n + 1)
dp[1] = 5
for i in range(2, n + 1):
    dp[i] = 5 * i + dp[i - 1] - (2 * (i - 1) + 1)
print(dp[-1] % 45678)