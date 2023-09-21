import heapq
T = int(input())

def dijkstra(s):
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0
    while pq:
        d, v = heapq.heappop(pq)
        if distance[v] < d:
            continue
        for i in range(N + 1):
            if G[v][i]:
                nd = d + G[v][i]
                if nd < distance[i]:
                    distance[i] = nd
                    heapq.heappush(pq, (nd, i))

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    G = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w
    distance = [float('inf')] * (N + 1)
    dijkstra(0)
    ans = distance[N]
    print(f'#{tc} {ans}')