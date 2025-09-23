import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * n
visited[r - 1] = 1
idx = 2
q = [r - 1]
while q:
    x = q.pop(0)
    for nx in sorted(graph[x], reverse=True):
        if visited[nx] == 0:
            q.append(nx)
            visited[nx] = idx
            idx += 1
print('\n'.join(map(str, visited)))