import sys
input = sys.stdin.readline
MAX = float('inf')
n, m, k, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
dist = [MAX] * (n + 1)
dist[x] = 0
for _ in range(k):
    for s, e in edges:
        if dist[s] != MAX and dist[e] > dist[s] + 1:
            dist[e] = dist[s] + 1
if dist.count(k) == 0: print(-1)
else:
    for i in range(1, n + 1):
        if dist[i] == k: print(i)