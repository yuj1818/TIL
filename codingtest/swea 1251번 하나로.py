import heapq

def prim(s):
    heap = []
    visited = [0] * N
    heapq.heappush(heap, (0, s))
    total_d = 0

    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            total_d += d
            for i in range(N):
                if i != v and not visited[i]:
                    heapq.heappush(heap, (G[v][i], i))
    return total_d

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    G = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j != i:
                G[i][j] = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
    ans = round(prim(0) + 0.000000000001)
    print(f'#{tc} {ans}')