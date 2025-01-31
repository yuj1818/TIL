import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])
# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y: return
    if x < y: parents[y] = x
    else: parents[x] = y

sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f-1) != find_set(t-1):
        sum_weight += w
        e = w
        union(f-1, t-1)
print(sum_weight - e)