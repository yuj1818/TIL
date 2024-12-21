import sys
input = sys.stdin.readline
n = int(input())
drinks = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 3)
for i in range(1, n + 1):
    dp[i + 2] = max(dp[i] + drinks[i], drinks[i - 1] + drinks[i] + dp[i - 1], dp[i + 1])
print(dp[-1])