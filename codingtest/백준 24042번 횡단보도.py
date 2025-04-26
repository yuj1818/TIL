from heapq import heappush, heappop
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

def dijkstra():
    visited = [0] * (n + 1)
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        t, x = heappop(pq)
        if visited[x]: continue
        elif x == n: return t
        visited[x] = 1
        for nx, nt in graph[x]:
            if visited[nx]: continue
            tt = (t - nt) // m
            if nt + tt * m < t: tt += 1
            nt = nt + tt * m + 1
            if dist[nx] > nt:
                dist[nx] = nt
                heappush(pq, (nt, nx))

print(dijkstra())