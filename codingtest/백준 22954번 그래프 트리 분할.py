import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def dfs(x):
    visited[x] = 1
    edges = []
    group = [x]
    s = [x]
    while s:
        x = s.pop()
        for i, nx in d_edges[x]:
            if not visited[nx]:
                visited[nx] = 1
                edges.append(i)
                group.append(nx)
                s.append(nx)
    return edges, group

def main():
    global visited, d_edges
    n, m = map(int, input().split())
    if n <= 2 or n - 2 > m:
        print(-1)
        return
    a_edges = [[i] + list(map(int, input().split())) for i in range(1, m + 1)]
    d_edges = {i:[] for i in range(1, n + 1)}
    for i, u, v in a_edges:
        d_edges[u].append((i, v))
        d_edges[v].append((i, u))
    visited = [0] * (n + 1)
    g_edges, groups, g_last = list(), list(), list()
    for i in range(1, n + 1):
        if not visited[i]:
            edges, group = dfs(i)
            g_edges.append(edges)
            groups.append(group)
            g_last.append(group[-1])
    if len(groups) > 2:
        print(-1)
        return
    elif len(groups) == 2:
        l1, l2 = len(groups[0]), len(groups[1])
        if l1 == l2:
            print(-1)
            return
        else:
            print(l1, l2)
            for i in range(2):
                print(' '.join(map(str, groups[i])))
                print(' '.join(map(str, g_edges[i])))
            return
    edges, group, last = *g_edges, *groups, *g_last
    e1 = list()
    for i in edges:
        _, u, v = a_edges[i - 1]
        if u != last and v != last: e1.append(i)
    group.pop()
    print(len(group), 1)
    print(' '.join(map(str, group)))
    print(' '.join(map(str, e1)))
    print(last)

main()