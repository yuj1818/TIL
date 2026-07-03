MIN = -float('inf')
n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]
mv = 0
for e, t in quests: mv += t
dp = [[MIN] * (mv + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i, (e, t) in enumerate(quests):
    for j in range(mv, -1, -1):
        if j >= t: dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - t] + e)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
ans = float('inf')
for i in range(mv + 1):
    if dp[n][i] >= m: ans = min(ans, i)
if ans == float('inf'): ans = -1
print(ans)
