T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    dp = [[N * M] * M for _ in range(N)]
    ans = 0
    # 위에서 아래로 탐색
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                dp[i][j] = 0
                continue
            for d in range(4):
                nj = j + dx[d]
                ni = i + dy[d]
                if 0 <= nj < M and 0 <= ni < N:
                    dp[i][j] = min(dp[ni][nj] + 1, dp[i][j])
    # 아래에서 위로 탐색
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if MAP[i][j] != 'W':
                for d in range(4):
                    nj = j + dx[d]
                    ni = i + dy[d]
                    if 0 <= nj < M and 0 <= ni < N:
                        dp[i][j] = min(dp[ni][nj] + 1, dp[i][j])
                if dp[i][j] != N * M:
                    ans += dp[i][j]
    print(f'#{tc} {ans}')