import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(s):
    mc = a[s]
    mp = s
    for w in graph[s]:
        if not visited[w]:
            visited[w] = 1
            cnt, cp = dfs(w)
            nc = a[s] + cnt
            if (mc < nc) or (mc == nc and mp > cp):
                mc = nc
                mp = cp
    return mc, mp

def main():
    global a, graph, visited
    n = int(input())
    a = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    visited = [0] * (n + 1)
    visited[1] = 1
    _, p = dfs(1)
    visited = [0] * (n + 1)
    visited[p] = 1
    rc, rp = dfs(p)
    print(rc, min(p, rp))

main()