import sys
input = sys.stdin.readline
n, m = map(int, input().split())
w = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
ans = 0
for i in range(n):
    for v in graph[i]:
        if w[v] >= w[i]: break
    else: ans += 1
print(ans)