from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    global maxV
    q = deque([s])
    visited = [0] * (n + 1)
    visited[s] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for w in graph[x]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
                cnt += 1
    if maxV < cnt: maxV = cnt
    return cnt

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
cnt = []
maxV = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
for i in range(1, n + 1): cnt.append(bfs(i))
for i in range(n):
    if cnt[i] == maxV: print(i + 1, end=' ')