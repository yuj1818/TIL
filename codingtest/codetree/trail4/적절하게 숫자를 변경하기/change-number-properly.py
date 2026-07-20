n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
dp = [[[-1] * 4 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(4):
    dp[1][m][i] = 1 if i == a[1] - 1 else 0
for i in range(2, n + 1):
    cur = a[i] - 1
    for j in range(m, -1, -1):
        for prev in range(4):
            if dp[i - 1][j][prev] == -1: continue
            for x in range(4):
                pt = 1 if cur == x else 0
                if x == prev:
                    dp[i][j][x] = max(dp[i][j][x], dp[i - 1][j][prev] + pt)
                elif j > 0:
                    dp[i][j - 1][x] = max(dp[i][j - 1][x], dp[i - 1][j][prev] + pt)

ans = 0
for i in range(m + 1):
    for j in range(4):
        if ans < dp[n][i][j]: ans = dp[n][i][j]
print(ans)