MIN = -float('inf')
n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[MIN] * (m + 1) for _ in range(n)]
for i in range(n): 
    if arr[i][0] == 1: dp[i][1] = 0
for i in range(2, m + 1):
    for j in range(n):
        s, e, v = arr[j]
        if i > e or i < s: continue
        for k in range(n):
            if dp[k][i - 1] == MIN: continue
            dp[j][i] = max(dp[j][i], dp[k][i - 1] + abs(v - arr[k][-1]))
print(max([x[-1] for x in dp]))