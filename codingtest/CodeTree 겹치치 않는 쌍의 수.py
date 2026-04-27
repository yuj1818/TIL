from itertools import combinations
n = int(input())
groups = []
for _ in range(n):
    _, *g = list(map(int, input().split()))
    r = 0
    for x in g: r |= 1 << x
    groups.append(r)

cnt = 0
for a, b in combinations(groups, 2):
    if a & b: continue
    cnt += 1
print(cnt)
