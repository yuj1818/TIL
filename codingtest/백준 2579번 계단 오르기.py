import sys
input = sys.stdin.readline
N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * (N)
for idx in range(N):
    if idx == 0:
        dp[idx] = stairs[idx]
    elif idx == 1:
        dp[idx] = stairs[idx] + stairs[idx - 1]
    else:
        dp[idx] = max(dp[idx - 2] + stairs[idx], dp[idx - 3] + stairs[idx - 1] + stairs[idx])
print(dp[N - 1])