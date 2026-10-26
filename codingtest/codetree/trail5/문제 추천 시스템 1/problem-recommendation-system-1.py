from sortedcontainers import SortedSet
n = int(input())
pa = SortedSet()
for _ in range(n):
    p, l = map(int, input().split())
    pa.add((l, p))
m = int(input())
for _ in range(m):
    s = input().split()
    if s[0] == 'rc':
        x = int(s[1])
        if x == 1: print(pa[-1][1])
        else: print(pa[0][1])
    elif s[0] == 'ad':
        pa.add((int(s[2]), int(s[1])))
    else:
        pa.remove((int(s[2]), int(s[1])))