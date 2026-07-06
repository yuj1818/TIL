MIN = -float('inf')
n = int(input())
coin = [0] + list(map(int, input().split()))
dp = [[MIN] * 4 for _ in range(n + 1)]
dp[0][0] = 0
dp[1][0] = MIN
dp[1][1] = coin[1]
dp[2][0] = coin[2]
for i in range(2, n + 1):
    for j in range(4):
        if j > 0 and i > 0 and dp[i - 1][j - 1] != MIN:
            dp[i][j] = dp[i - 1][j - 1] + coin[i]
        if i > 1 and dp[i - 2][j] != MIN:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
print(max(dp[-1]))