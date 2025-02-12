import sys

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
s = [r]
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

while s:
    x = s.pop()
    if not visited[x]:
        cnt += 1
        visited[x] = cnt
        for w in graph[x]:
            if not visited[w]:
                s.append(w)

for i in range(1, n + 1):
    print(visited[i])