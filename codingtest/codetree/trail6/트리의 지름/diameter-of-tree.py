def find(s):
    dist = [-1] * (n + 1)            
    dist[s] = 0
    stack = [s]
    while stack:
        x = stack.pop()
        for nxt, w in edges[x]:
            if dist[nxt] != -1: continue
            dist[nxt] = dist[x] + w
            stack.append(nxt)
    res = s
    for i in range(1, n + 1):
        if dist[i] > dist[res]: res = i
    return res, dist[res]

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))
    edges[e].append((s, w))
u, _ = find(1)
_, ans = find(u)
print(ans)