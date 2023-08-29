from collections import deque
N, M, V = map(int, input().split())
adj_l = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    adj_l[n1].append(n2)
    adj_l[n2].append(n1)

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for w in sorted(adj_l[v]):
        if not visited[w]:
            dfs(w)

def bfs(v):
    visited = [0] * (N + 1)
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        t = q.popleft()
        print(t, end=' ')
        for w in sorted(adj_l[t]):
            if not visited[w]:
                q.append(w)
                visited[w] = 1

visited = [0] * (N + 1)
stack = [V]
dfs(V)
print()
bfs(V)