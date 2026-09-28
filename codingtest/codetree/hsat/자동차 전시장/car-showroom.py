from collections import deque
n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
points = list(map(int, input().split()))
max_dist = [0] * (n + 1)
cnt = [0] * (n + 1)
for p in points:
    dist = [-1] * (n + 1)
    dist[p] = 0
    q = deque([p])

    while q:
        x = q.popleft()
        for nxt in edges[x]:
            if dist[nxt] == -1:
                dist[nxt] = dist[x] + 1
                q.append(nxt)
    
    for i in range(1, n + 1):
        if dist[i] == -1: continue
        cnt[i] += 1
        if dist[i] > max_dist[i]: max_dist[i] = dist[i]

MAX = float('inf')
ans = MAX

for i in range(1, n + 1):
    if cnt[i] != k: continue
    if max_dist[i] < ans: ans = max_dist[i]

if ans == MAX: print(-1)
else: print(ans)
