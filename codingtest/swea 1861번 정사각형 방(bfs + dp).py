from collections import deque
T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def calc_dist(y, x):
    global max_dist, max_r_n
    q = deque()
    cnt = 1
    q.append((y, x))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and rooms[r][c] + 1 == rooms[nr][nc]:
                if dp[r][c]:
                    cnt += dp[r][c] - 1
                else:
                    q.append((nr, nc))
                    cnt += 1
                break
    dp[y][x] = cnt
    if dp[y][x] != 1:
        if max_dist == cnt:
            max_r_n = rooms[y][x] if rooms[y][x] < max_r_n else max_r_n
        elif max_dist < cnt:
            max_dist = cnt
            max_r_n = rooms[y][x]

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    max_dist = 1
    max_r_n = N ** 2
    dp = [[0] * N for _ in range(N)] # 시작점이 Aij일 때 이동할 수 있는 방 수
    for i in range(N):
        for j in range(N):
            calc_dist(i, j)
    print(f'#{tc} {max_r_n} {max_dist}')