INF = 120
def solution(info, n, m):
    l = len(info)
    dp = [[INF] * m for _ in range(l)]
    dp[0][0] = info[0][0]
    if info[0][1] < m: dp[0][info[0][1]] = 0
    if l == 1: return 0 if info[0][1] < m else info[0][0]
    for i in range(1, l):
        a, b = info[i]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
    ans = INF
    for i in range(m): ans = min(ans, dp[-1][i])
    return ans if ans < n else -1