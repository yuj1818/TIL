import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y

def union_by_rank(x, y):
    x = find(x)
    y = find(y)

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

for _ in range(m):
    s, e = map(int, input().split())
    union_by_rank(s, e)

cnt = 0

for i in range(1, n + 1):
    if i == find(i):
        cnt += 1

print(cnt)