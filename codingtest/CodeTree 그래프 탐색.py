def dfs(x):
    global cnt
    for nx in graph[x]:
        if not visited[nx]:
            cnt += 1
            visited[nx] = 1
            dfs(nx)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0] * (n + 1)
visited[1] = 1
cnt = 0
dfs(1)
print(cnt)
