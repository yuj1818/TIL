import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
v, e = map(int, input().split())
edge = []
for _ in range(e):
    s, e, w = map(int, input().split())
    edge.append([s, e, w])
edge.sort(key=lambda x: x[2])
parents = [i for i in range(v + 1)]

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

t = 0
for s, e, w in edge:
    if find(s) != find(e):
        t += w
        union(s, e)

print(t)