n = int(input())
profit = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for x in range(1, n + 1):
        if i < x: continue
        dp[i] = max(dp[i], dp[i - x] + profit[x])
print(dp[-1])