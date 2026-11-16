n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
dist = [float('inf')] * (n + 1)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = w
dist[1] = 0
for i in range(1, n + 1):
    min_idx = -1
    for j in range(1, n + 1):
        if visited[j]: continue
        if min_idx == -1 or dist[min_idx] > dist[j]: min_idx = j
    visited[min_idx] = 1
    for j in range(1, n + 1):
        if graph[min_idx][j] == 0: continue
        dist[j] = min(dist[j], dist[min_idx] + graph[min_idx][j])
for i in range(2, n + 1):
    if dist[i] == float('inf'): print(-1)
    else: print(dist[i])