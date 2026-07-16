MOD = 10 ** 9 + 7
n = int(input())
dp = [[0] * 11 for _ in range(n)]
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
for i in range(1, n):
    for j in range(10):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD
print((sum(dp[-1]) - dp[-1][0]) % MOD)