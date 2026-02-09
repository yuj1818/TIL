n = int(input())
if n < 3:
    print(n)
    exit()
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[-1])
