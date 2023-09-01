from collections import deque

def bfs(s):
    q = deque()
    visited = [0] * (N + 1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.popleft()
        for w in trees[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
    return visited.count(1) - 1

N = int(input())
n_pair = int(input())
trees = [[] for _ in range(N + 1)]
for _ in range(n_pair):
    s, e = map(int, input().split())
    trees[s].append(e)
    trees[e].append(s)
print(bfs(1))
