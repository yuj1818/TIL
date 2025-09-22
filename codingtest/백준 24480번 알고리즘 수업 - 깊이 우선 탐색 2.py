import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x):
    global idx
    for nx in sorted(graph[x], reverse=True):
        if not visited[nx]:
            visited[nx] = 1
            seq[nx] = idx
            idx += 1
            dfs(nx)

idx = 2
n, m, r = map(int, input().split())
seq = [0] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * n
visited[r-1] = 1
seq[r-1] = 1
s = [r-1]
dfs(r-1)
print('\n'.join(map(str, seq)))