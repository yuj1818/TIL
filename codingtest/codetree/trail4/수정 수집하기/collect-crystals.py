n, k = map(int, input().split())
s = input()
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    pos = 0 if s[i - 1] == 'L' else 1
    for j in range(k + 1):
        cur = j % 2
        pt = 1 if cur == pos else 0
        dp[i][j] = dp[i - 1][j] + pt
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + pt)
print(max(dp[-1]))