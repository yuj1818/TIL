from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
c, h, k = map(int, input().split())

def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x < y: parents[y] = x
    else: parents[x] = y

parents = [i for i in range(n + 1)]
for i in range(1, n + 1):
    for j in graph[i]:
        if find(i) == find(j): continue
        union(i, j)

team = defaultdict(int)
cr, hr = -1, -1
for i in range(1, n + 1):
    r = find(i)
    team[r] += 1
    if i == c: cr = i
    if i == h: hr = i

ans = team[cr]
for num, cnt in sorted(team.items(), key=lambda item: item[1], reverse=True):
    if num == hr or num == cr: continue
    if k <= 0: break
    ans += cnt
    k -= 1
print(ans)
