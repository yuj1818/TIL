from itertools import combinations

def find_root(idx):
    ni = idx
    for i in range(h, 0, -1):
        if graph[i][ni]:
            ni -= 1
        elif ni < n - 1 and graph[i][ni + 1]:
            ni += 1
    return ni

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
h = max([y for _, y in edges])
graph = [[0] * n for _ in range(h + 1)]
for x, y in edges: graph[y][x] = 1
ans = [find_root(i) for i in range(n)]
mv = m
for i in range(m):
    for comb in combinations(edges, i):
        graph = [[0] * n for _ in range(h + 1)]
        for x, y in comb: graph[y][x] = 1
        for j in range(n):
            root = find_root(j)
            if ans[j] != root: break
        else:
            mv = i
            break
    if mv != m: break
print(mv)
