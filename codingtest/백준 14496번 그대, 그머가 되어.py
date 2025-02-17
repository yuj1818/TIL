import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [0] * (n + 1)
    visited[a] = 1
    stk = [a]
    for c in range(n):
        tmp = []
        while stk:
            x = stk.pop()
            if x == b:
                return c
            for w in graph[x]:
                if not visited[w]:
                    tmp.append(w)
                    visited[w] = 1
        stk = tmp
    return -1

print(main())