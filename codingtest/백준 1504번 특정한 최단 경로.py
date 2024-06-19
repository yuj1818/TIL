import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
for _ in range(e) :
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])
v1, v2 = map(int, input().split())
INF = int(1e9)

def dijkstra(s):
    distance = [INF] * (n + 1)
    distance[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if distance[nxt] > new_cost:
                distance[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))
    return distance

dv1 = dijkstra(v1)
dv2 = dijkstra(v2)
ans = min(dv1[1] + dv1[v2] + dv2[-1], dv2[1] + dv2[v1] + dv1[-1])
print(ans if ans < INF else -1)