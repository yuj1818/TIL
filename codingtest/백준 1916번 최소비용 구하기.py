import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            n_cost = distance[now] + cost
            if distance[nxt] > n_cost:
                distance[nxt] = n_cost
                heapq.heappush(hq, (n_cost, nxt))

    return distance

s, e = map(int, input().split())
print(dijkstra(s)[e])