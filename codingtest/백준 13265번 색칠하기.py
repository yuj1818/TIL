import sys
input = sys.stdin.readline

def bfs(x):
    q = [x]
    color[x] = 1
    while q:
        x = q.pop(0)
        for nx in graph[x]:
            if color[nx] == -1:
                color[nx] = 1 if color[x] == 2 else 2
                q.append(nx)
            elif color[nx] == color[x]: return False
    return True

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    color = [-1] * (n + 1)
    for x in range(1, n + 1):
        if color[x] == -1:
            if not bfs(x):
                print('impossible')
                break
    else: print('possible')