import sys
n, m = map(int, sys.stdin.readline().split())
floor = set(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
tmp, pre = 0, 1
for i in range(1, n + 1):
    if i in floor:
        dp[i] = dp[i - 1]
    else:
        d = dp[i - 1] + 7
        c = tmp + (i - pre + 1) * 2 + 5
        if c > d:
            tmp = dp[i - 1]
            pre = i
            dp[i] = d
        else:
            dp[i] = c
print(dp[-1])