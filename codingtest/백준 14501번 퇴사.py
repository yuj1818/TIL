n = int(input())
dp = [0] * n
for i in range(n):
    t, p = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])
    if t <= n - i:
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)
print(dp[-1])