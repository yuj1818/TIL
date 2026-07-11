MOD = 10 ** 9 + 7
n = int(input())
dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
dp[0][0][0] = 1
dp[0][1][0] = 1
dp[0][0][1] = 1
for i in range(n):
    for j in range(3):
        for k in range(3):
            dp[i + 1][j + 1][0] = (dp[i + 1][j + 1][0] + dp[i][j][k]) % MOD
            dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) %  MOD
            if k != 2:
                dp[i + 1][j][k + 1] = (dp[i + 1][j][k + 1] + dp[i][j][k]) % MOD
ans =0 
for i in range(3):
    for j in range(3):
        ans = (ans + dp[n - 1][i][j]) % MOD
print(ans)