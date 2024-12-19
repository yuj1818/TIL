import sys
input = sys.stdin.readline

def main():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
    depth = [-1] * (n + 1)
    depth[r] = 0
    visited = [0] * (n + 1)
    stack = [r]
    while stack:
        s = stack.pop()
        if visited[s]: continue
        visited[s] = 1
        for x in graph[s]:
            if not visited[x]:
                stack.append(x)
                depth[x] = depth[s] + 1
    print(*depth[1:], sep='\n')

main()