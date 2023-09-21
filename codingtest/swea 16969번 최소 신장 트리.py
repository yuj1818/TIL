import heapq

T = int(input())

def mst_prim(s):
    heap = []
    visited = [0] * (V + 1)
    heapq.heappush(heap, (0, s))
    total_w = 0

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            total_w += w
            for i in range(V + 1):
                if G[v][i] and not visited[i]:
                    heapq.heappush(heap, (G[v][i], i))
    return total_w

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w  = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w
    ans = mst_prim(0)
    print(f'#{tc} {ans}')