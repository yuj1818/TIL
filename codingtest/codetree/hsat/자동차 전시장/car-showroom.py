from collections import deque
n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
start_points = list(map(int, input().split()))
max_dist_to = [0] * (n + 1)
reach_count = [0] * (n + 1)
for p in start_points:
    dist = [-1] * (n + 1)
    q = deque([p])
    dist[p] = 0
    
    while q:
        x = q.popleft()
        for nxt in edges[x]:
            if dist[nxt] == -1:
                dist[nxt] = dist[x] + 1
                q.append(nxt)
    
    for i in range(1, n + 1):
        if dist[i] != -1:
            reach_count[i] += 1
            if dist[i] > max_dist_to[i]:
                max_dist_to[i] = dist[i]

ans = float('inf')
best_loc = -1

for i in range(1, n + 1):
    if reach_count[i] == k:
        if max_dist_to[i] < ans:
            ans = max_dist_to[i]
            best_loc = i
        elif max_dist_to[i] == ans:
            if best_loc == -1 or i < best_loc:
                best_loc = i

if ans == float('inf'): print(-1)
else: print(ans)
