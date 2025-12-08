import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  u, v = map(int, input().split())
  graph[u][v] = 1

for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(1, n + 1):
      if graph[j][k] or (graph[j][i] and graph[i][k]): graph[j][k] = 1

ans = 0
for i in range(1, n + 1):
  cnt = 0
  for j in range(1, n + 1):
    cnt += graph[i][j] + graph[j][i]
  if cnt == n - 1: ans += 1
print(ans)