n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (m + 1)
dp[0] = 1
for x in arr:
    for i in range(m, -1, -1):
        if i >= x:
            if dp[i - x] != 0: dp[i] += dp[i - x]
if dp[-1]: print('Yes')
else: print('No')