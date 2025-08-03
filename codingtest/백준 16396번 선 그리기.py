import sys
input = sys.stdin.readline
n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])
phase = [a[0]]
for i in range(1, n):
    cs, ce = phase[-1]
    ns, ne = a[i]
    if ce < ns: phase.append([ns, ne])
    elif ce < ne: phase[-1][1] = ne
print(sum([e - s for s, e in phase]))