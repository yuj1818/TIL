import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(m)]] + [[[INF] * 3 for _ in range(m)] for _ in range(n)]

for i in range(1, n + 1):
    for j in range(m):
        if 0 < j:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + graph[i - 1][j]
        if j + 1 < m:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i - 1][j]
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i - 1][j]

ans = INF
for line in dp[-1]:
    for v in line:
        ans = min(ans, v)
print(ans)