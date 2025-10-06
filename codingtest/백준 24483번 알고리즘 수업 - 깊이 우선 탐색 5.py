import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x):
    global idx
    for nx in sorted(graph[x]):
        if visited[nx] == [-1, 0]:
            visited[nx] = [visited[x][0] + 1, idx]
            idx += 1
            dfs(nx)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [[-1, 0] for _ in range(n)]
visited[r - 1] = [0, 1]
idx = 2
dfs(r - 1)
print(sum(map(lambda x: x[0] * x[1], visited)))