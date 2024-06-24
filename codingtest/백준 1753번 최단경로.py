import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
v, e = map(int, input().split())
s = int(input())
connection = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    a, b, w = map(int, input().split())
    connection[a].append([b, w])

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for n, c in connection[now]:
            nc = dist + c
            if distance[n] > nc:
                distance[n] = nc
                heapq.heappush(hq, (nc, n))

dijkstra(s)
for i in range(1, v + 1):
    print(distance[i] if distance[i] < 1000000000 else 'INF')