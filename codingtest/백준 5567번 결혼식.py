import sys
input = sys.stdin.readline
n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
invited = [0] * (n + 1)
q = [(1, 0)]
invited[1] = 1
while q:
    x, d = q.pop(0)
    if d == 2: continue
    for nx in graph[x]:
        if not invited[nx]:
            invited[nx] = 1
            q.append((nx, d + 1))
print(sum(invited) - 1)