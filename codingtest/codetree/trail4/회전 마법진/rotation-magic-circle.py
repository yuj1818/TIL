INF = float('inf')
n = int(input())
cur = input()
tar = input()
dp = [[INF] * 10 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(10):
        if dp[i][j] == INF: continue
        c = (int(cur[i]) + j) % 10
        t = int(tar[i])
        cost = (t - c + 10) % 10
        nj = (j + cost) % 10
        dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + cost)
        cost = (c - t + 10) % 10
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost)
print(min(dp[-1]))