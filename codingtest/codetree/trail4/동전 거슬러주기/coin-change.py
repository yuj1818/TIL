n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp = [float('inf')] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    for c in coin:
        if i >= c:
            dp[i] = min(dp[i], dp[i - c] + 1)
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])