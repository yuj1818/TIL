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

for _ in range(1, v + 1):
    arr = list(map(int, input().split()))
    n = arr[0]
    for i in range(1, len(arr) - 1, 2):
        connection[n].append((arr[i], arr[i + 1]))

visited[1] = 1
dfs(1, 0)
visited = [0] * (v + 1)
visited[ln] = 1
dfs(ln, 0)

print(ans)