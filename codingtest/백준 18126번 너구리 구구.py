import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dist = [0] * (n + 1)
visited = [0] * (n + 1)
q = [(1, 0)]
visited[1] = 1
while q:
    x, d = q.pop(0)
    for nx, nd in graph[x]:
        if not visited[nx]:
            dist[nx] = d + nd
            visited[nx] = 1
            q.append((nx, d + nd))
print(max(dist))