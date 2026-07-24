INF = float('inf')
N, M, K = map(int, input().split())
dp = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, M + 1): dp[1][i][i] = 1
for i in range(1, N):
    for j in range(1, M + 1):
        for k in range(1, M + 1):
            for l in range(1, k + 1):
                if j + l > M: break
                dp[i + 1][j + l][l] += dp[i][j][k]
                dp[i + 1][j + 1][l] = min(dp[i + 1][j + l][l], INF)
cl, cm = 1, M
for i in range(N, 0, -1):
    while dp[i][cm][cl] < K:
        K -= dp[i][cm][cl]
        cl += 1
    print(cl, end=' ')
    cm -= cl