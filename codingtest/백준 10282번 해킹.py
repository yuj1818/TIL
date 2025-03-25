import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())

def virus(s):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])
    while q:
        x = q.popleft()
        for w, t in graph[x]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[x] + t
            else:
                if visited[w] > visited[x] + t:
                    visited[w] = visited[x] + t
                    q.append(w)
    return n - visited.count(0) + 1, max(visited) - 1

for _ in range(tc):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    print(*virus(c))