import sys
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bf(s):
    dist[s] = 0
    for i in range(n):
        for now, nxt, cost in edges:
            if dist[now] != INF and dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost
                if i == n - 1:
                    return True
    return False
isInf = bf(1)
if isInf: print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF: print(-1)
        else: print(dist[i])