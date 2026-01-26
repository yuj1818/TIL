import sys
h, y = map(int, sys.stdin.readline().split())
dp = [0] * (y + 1)
dp[0] = h
for i in range(1, y + 1):
    if i < 3:
        dp[i] = int(dp[i - 1] * 1.05)
        continue
    dp[i] = int(max(((dp[i - 5] * 1.35) if i > 4 else 0), dp[i - 3] * 1.2, dp[i - 1] * 1.05))
print(dp[-1])