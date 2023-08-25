from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())
def calculate_profit(i, j):
    global max_home
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    # k가 1일 때
    if city[i][j] == 1 and city[i][j] - 1 >= 0:
        max_home = max(max_home, 1)
    cnt = city[i][j]
    k = 2
    while k <= N + 2:   # 똑같은 좌표에서 거리만 늘려가면서 이전의 거리에서 카운팅한 집 수 누적
        expense = k * k + (k - 1) * (k - 1)
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                nr = r + dy[d]
                nc = c + dx[d]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    if city[nr][nc] == 1:
                        cnt += 1
        if cnt * M - expense >= 0:
            max_home = max(max_home, cnt)
        k += 1

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    max_home = 0
    for i in range(N):
        for j in range(N):
            calculate_profit(i, j)
    print(f'#{tc} {max_home}')