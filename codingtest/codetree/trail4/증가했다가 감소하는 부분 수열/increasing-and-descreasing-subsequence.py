n = int(input())
a = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]: dp[i][0] = max(dp[i][0], dp[j][0] + 1)
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j]: dp[i][1] = max(dp[i][1], dp[j][1] + 1)
ans = 0
for i in range(n):
    ans = max(ans, dp[i][0] + dp[i][1] - 1)
print(ans)