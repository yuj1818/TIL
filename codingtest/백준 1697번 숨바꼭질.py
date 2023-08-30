from collections import deque
N, K = map(int, input().split())
def bfs(s):
    global min_v
    q = deque()
    visited = [0] * 200001
    q.append(s)
    visited[s] = 1
    while q:
        t = q.popleft()
        if t == K:
            min_v = min(min_v, visited[t] - 1)
            return
        for w in [t + 1, t - 1, t * 2]:
            if 0 <= w < 200000 and not visited[w]:
                visited[w] = visited[t] + 1
                q.append(w)

min_v = 100000
bfs(N)
print(min_v)