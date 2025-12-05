import sys
input = sys.stdin.readline

def bfs(v):
  visited = [0] * (n + 1)
  visited[s] = 1
  q = [s]
  while q:
    x = q.pop(0)
    if x == e: return True
    for nx, nw in graph[x]:
      if not visited[nx] and mid <= nw:
        q.append(nx)
        visited[nx] = 1
  return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
max_w = 0
for _ in range(m):
  s, e, w = map(int, input().split())
  max_w = max(max_w, w)
  graph[s].append((e, w))
  graph[e].append((s, w))
s, e = map(int, input().split())
l, r = 0, max_w
while l <= r:
  mid = (l + r) // 2
  if bfs(mid): l = mid + 1
  else: r = mid - 1

print(r)