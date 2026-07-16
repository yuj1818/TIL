MIN = -float('inf')
n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[MIN] * n for _ in range(m + 1)]
for i in range(n):
    if arr[i][0] == 1: dp[1][i] = 0
for i in range(2, m + 1):
    for j in range(n):
        s, e, v = arr[j]
        if i > e or i < s: continue
        for k in range(n):
            if dp[i - 1][k] == MIN: continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v - arr[k][-1]))
print(max(dp[-1]))