from collections import defaultdict
m = int(input())
edges = defaultdict(list)
nodes = set()
for _ in range(m):
    a, b = map(int, input().split())
    nodes.add(a)
    nodes.add(b)
    edges[a].append(b)
nodes = sorted(nodes)
par = {x: 0 for x in nodes}
visited = {x: 0 for x in nodes}

def check():
    root = 0
    for k, v in edges.items():
        for x in v: par[x] += 1
    for x, cnt in par.items():
        if cnt == 0:
            if root: return 0
            root = x
        if cnt > 1: return 0
    visited[root] = 1
    q = [root]
    while q:
        x = q.pop(0)
        for nxt in edges[x]:
            visited[nxt] += 1
            q.append(nxt)
    for x, cnt in visited.items():
        if cnt == 0: return 0
    return 1

print(check())