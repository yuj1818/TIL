import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
leaf = [i for i in range(n + 1) if len(graph[i]) == 1]
visited = [0] * (n + 1)
while leaf:
    x = leaf.pop()
    if not graph[x]: continue
    p = graph[x][0]
    for gp in graph[p]:
        graph[gp].remove(p)
        if len(graph[gp]) == 1: leaf.append(gp)
    visited[p] = 1
    graph[p] = []
print(sum(visited))