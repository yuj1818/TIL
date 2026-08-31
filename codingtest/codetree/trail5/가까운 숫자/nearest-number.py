from sortedcontainers import SortedSet
n = int(input())
pt = SortedSet([0])
cnt, mv = 1, float('inf')
for x in list(map(int, input().split())):
    nv = float('inf')
    r = pt.bisect_right(x)
    if r < cnt: nv = pt[r] - x
    l = r - 1
    if l >= 0: nv = min(nv, x - pt[l])
    pt.add(x)
    cnt += 1
    mv = min(mv, nv)
    print(mv)