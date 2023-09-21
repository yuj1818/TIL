import heapq
T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dijkstra(sx, sy):
    heap = []
    heapq.heappush(heap, (0, (sx, sy)))
    distance[sy][sx] = 0
    while heap:
        d, v = heapq.heappop(heap)
        x, y = v
        if distance[y][x] < d:
            continue
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]
            if 0 <= nx < N and 0 <= ny < N:
                nd = d + G[ny][nx]
                if distance[ny][nx] > nd:
                    distance[ny][nx] = nd
                    heapq.heappush(heap, (nd, (nx, ny)))

for tc in range(1, T + 1):
    N = int(input())
    G = [list(map(int, input())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]
    dijkstra(0, 0)
    ans = distance[N - 1][N - 1]
    print(f'#{tc} {ans}')