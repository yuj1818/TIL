import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())

def find_min(s_x, s_y):
    pq = []
    heapq.heappush(pq, (0, (s_x, s_y)))
    fuel[s_y][s_x] = 0

    while pq:
        f, n = heapq.heappop(pq)
        if fuel[n[1]][n[0]] < f:
            continue
        for d in range(4):
            nx = n[0] + dx[d]
            ny = n[1] + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if G[ny][nx] > G[n[1]][n[0]]:
                    nf = G[ny][nx] - G[n[1]][n[0]] + 1
                else:
                    nf = 1
                tf = f + nf
                if fuel[ny][nx] <= tf:
                    continue
                fuel[ny][nx] = tf
                heapq.heappush(pq, (tf, (nx, ny)))

for tc in range(1, T + 1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[float('inf')] * N for _ in range(N)]
    find_min(0, 0)
    ans = fuel[N - 1][N - 1]
    print(f'#{tc} {ans}')