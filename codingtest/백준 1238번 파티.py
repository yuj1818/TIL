import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
r_graph = [[] for _ in range(n + 1)]
for _ in range(m) :
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    r_graph[e].append([s, w])
INF = int(1e9)

def dijkstra(s, edges):
    distance = [INF] * (n + 1)
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for nxt, cost in edges[now]:
            new_cost = dist + cost
            if distance[nxt] > new_cost:
                distance[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))
    return distance

n2x = dijkstra(x, r_graph)
x2n = dijkstra(x, graph)

print(max([n2x[i] + x2n[i] for i in range(1, n + 1) if i != x]))