import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
visited = [0] * n

def check():
    for a in range(n):
        visited[a] = 1
        for b in graph[a]:
            if not visited[b]:
                visited[b] = 1
                for c in graph[b]:
                    if not visited[c]:
                        visited[c] = 1
                        for d in graph[c]:
                            if not visited[d]:
                                visited[d] = 1
                                for e in graph[d]:
                                    if not visited[e]:
                                        return 1
                                visited[d] = 0
                        visited[c] = 0
                visited[b] = 0
        visited[a] = 0
    return 0

print(check())