from collections import deque
N, M = map(int, input().split())
adj_l = [[] for _ in range(N + 1)]
for _ in range(M):
    p1, p2 = map(int, input().split())
    adj_l[p1].append(p2)
    adj_l[p2].append(p1)
adj_l = [list(set(l)) for l in adj_l]

def bfs(v):
    q = deque()
    visited = [0] * (N + 1)
    q.append(v)
    visited[v] = 1
    while q:
        t = q.popleft()
        for w in adj_l[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1
    return sum(visited) - N

min_v = (N - 1) ** 2
ans = []

for i in range(1, N + 1):
    kb = bfs(i)
    if min_v == kb:
        ans.append(i)
    elif min_v > kb:
        min_v = kb
        ans = [i]

print(sorted(ans)[0])