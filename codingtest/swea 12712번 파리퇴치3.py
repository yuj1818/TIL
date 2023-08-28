T = int(input())
dx = [0, 0, -1, 1]    # 상 하 좌 우
dy = [-1, 1, 0, 0]
cx = [-1, 1, 1, -1]   # 좌상 우상 우하 좌하
cy = [-1, -1, 1, 1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_n = 0
    for i in range(N):
        for j in range(N):
            plus_n = flies[i][j]
            cross_n = flies[i][j]
            for m in range(1, M):
                for d in range(4):
                    ni = i + dy[d] * m
                    nj = j + dx[d] * m
                    ci = i + cy[d] * m
                    cj = j + cx[d] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        plus_n += flies[ni][nj]
                    if 0 <= ci < N and 0 <= cj < N:
                        cross_n += flies[ci][cj]
            max_n = max(max_n, plus_n, cross_n)
    print(f'#{tc} {max_n}')
