import sys

m = int(input())
s = set()

for _ in range(m):
    l = sys.stdin.readline().split()
    f, n = l if len(l) > 1 else (l[0], 0)
    n = int(n)

    if f == 'add':
        s.add(n)
    elif f == 'remove':
        s.discard(n)
    elif f == 'check':
        print(1 if s & {n} else 0)
    elif f == 'toggle':
        if s & {n}:
            s.remove(n)
        else:
            s.add(n)
    elif f == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s = set([])