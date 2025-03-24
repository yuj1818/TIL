import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, graph):
    global cnt
    visited[x] = 1
    for w in graph[x]:
        if not visited[w]: dfs(w, graph)
    res[cnt] = x
    cnt -= 1

def main():
    global cnt, visited, res
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    visited = [0] * (n + 1)
    res = [0] * n
    cnt = n - 1
    for i in range(1, n + 1):
        if not visited[i]: dfs(i, graph)
    print(*res)

main()