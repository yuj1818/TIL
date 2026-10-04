def dfs(x, p):
    if not graph[x]: leaf[x] += 1
    for nxt in graph[x]:
        dfs(nxt, x)
        leaf[x] += leaf[nxt]

n = int(input())
par = list(map(int, input().split()))
r = int(input())
graph = [set() for _ in range(n)]
leaf = [0] * n
root = 0
for i in range(n):
    if par[i] == -1:
        root = i
        continue
    graph[par[i]].add(i)
for i in range(n):
    if r in graph[i]: graph[i].remove(r)
if root != r:
    dfs(root, -1)
print(leaf[root])