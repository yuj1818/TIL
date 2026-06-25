n = int(input())
a = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        if a[j] > a[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    dp[i][1] = max(dp[i][1], dp[i][0])
print(max(dp, key=lambda x: x[1])[1])