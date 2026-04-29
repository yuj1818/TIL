n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * (n + 1) for _ in range(n + 1)]
ans = -1000 * (n ** 2)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + arr[i - 1][j - 1]
for y1 in range(1, n + 1):
    for y2 in range(y1, n + 1):
        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            total = acc[y2][x] - acc[y2][x - 1] - acc[y1 - 1][x] + acc[y1 - 1][x - 1]
            dp[x] = max(total, dp[x - 1] + total)
        ans = max(ans, max(dp[1:]))
print(ans)
