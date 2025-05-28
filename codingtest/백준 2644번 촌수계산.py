import sys
input = sys.stdin.readline

def dfs(x):
    if x == b:
        print(visited[x])
        sys.exit()
    for w in graph[x]:
        if visited[w] >= 0: continue
        visited[w] = visited[x] + 1
        dfs(w)

def main():
    global b, visited, graph
    n = int(input())
    a, b = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(int(input())):
        p, c = map(int, input().split())
        graph[p].append(c)
        graph[c].append(p)
    visited = [-1] * (n + 1)
    visited[a] = 0
    dfs(a)
    print(-1)

main()