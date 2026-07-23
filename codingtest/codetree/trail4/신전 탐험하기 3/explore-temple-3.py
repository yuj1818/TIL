MIN = -float('inf')
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[MIN] * m for _ in range(n + 1)]
for i in range(m): dp[0][i] = 0
for i in range(1, n + 1):
    for j in range(m):
        for k in range(m):
            if j == k: continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + arr[i - 1][j])
print(max(dp[-1]))