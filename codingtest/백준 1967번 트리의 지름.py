import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v = int(input())
connection = defaultdict(list)
visited = [0] * (v + 1)
ans = 0
ln = 0

def dfs(s, l):
    global ans, ln

    for e, w in connection[s]:
        if not visited[e]:
            visited[e] = 1
            dfs(e, l + w)

    if ans < l:
        ans, ln = l, s

for _ in range(v - 1):
    a, b, c = map(int, input().split())
    connection[a].append((b, c))
    connection[b].append((a, c))

visited[1] = 1
dfs(1, 0)
visited = [0] * (v + 1)
visited[ln] = 1
dfs(ln, 0)

print(ans)