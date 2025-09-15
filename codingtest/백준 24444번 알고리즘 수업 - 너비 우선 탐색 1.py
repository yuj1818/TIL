import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
q = [r]
visited = [0] * (n + 1)
visited[r] = 1
seq = [0] * n
idx = 1
while q:
    x = q.pop(0)
    seq[x - 1] = idx
    idx += 1
    for w in sorted(graph[x]):
        if not visited[w]:
            q.append(w)
            visited[w] = 1
print('\n'.join(map(str, seq)))