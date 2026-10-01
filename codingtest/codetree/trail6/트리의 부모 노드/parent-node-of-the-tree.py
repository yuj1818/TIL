def dfs(x):
    for nxt in edges[x]:
        if par[nxt] != 0: continue
        par[nxt] = x
        dfs(nxt)

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)
par = [0] * (n + 1)
par[1] = 1
dfs(1)
for i in range(2, n + 1): print(par[i])