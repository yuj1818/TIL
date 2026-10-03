import sys
sys.setrecursionlimit(10 ** 6)

def dfs(s):
    for nxt, w in edges[s]:
        if dist[nxt] != -1: continue
        dist[nxt] = dist[s] + w
        dfs(nxt)

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))
    edges[e].append((s, w))
dist = [-1] * (n + 1)
dist[1] = 0
dfs(1)
x, mv = -1, -1
for i in range(1, n + 1):
    if dist[i] > mv: x, mv = i, dist[i]
dist = [-1] * (n + 1)
dist[x] = 0
dfs(x)
print(max(dist))