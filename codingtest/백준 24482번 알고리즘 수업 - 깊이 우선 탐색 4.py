import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x):
    for nx in sorted(graph[x], reverse=True):
        if visited[nx] == -1:
            visited[nx] = visited[x] + 1
            dfs(nx)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1] * n
visited[r - 1] = 0
dfs(r - 1)
print('\n'.join(map(str, visited)))