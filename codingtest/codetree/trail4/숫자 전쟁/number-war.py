n = int(input())
p1 = [0] + list(map(int, input().split()))
p2 = [0] + list(map(int, input().split()))
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1: continue
        if p1[i + 1] < p2[j + 1]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if p1[i + 1] > p2[j + 1]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + p2[j + 1])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

ans = 0
for i in range(n + 1):
    ans = max(ans, max(dp[i]))
print(ans)