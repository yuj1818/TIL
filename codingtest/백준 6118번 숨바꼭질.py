import sys
input = sys.stdin.readline

def bfs():
    num, max_d, cnt = 1, 0, 0
    q = [(1, 0)]
    visited = [0] * (n + 1)
    visited[1] = 1
    while q:
        x, d = q.pop(0)
        sig = False
        for nx in graph[x]:
            if not visited[nx]:
                q.append((nx, d + 1))
                visited[nx] = 1
                sig = True
        if not sig:
            if d > max_d:
                max_d = d
                cnt = 1
                num = x
            elif d == max_d:
                num = min(num, x)
                cnt += 1
    return num, max_d, cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(*bfs())