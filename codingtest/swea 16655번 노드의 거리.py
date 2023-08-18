T = int(input())
def bfs(s, G, V):
    visited = [0] * (V + 1)
    q = list()
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t] - 1
        for w in adj_l[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1
    return 0

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    adj_l = [[] for _ in range(V + 1)]
    S, G = map(int, input().split())
    for v1, v2 in arr:
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    print(f'#{tc} {bfs(S, G, V)}')