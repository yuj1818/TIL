from sortedcontainers import SortedSet
for _ in range(int(input())):
    s = SortedSet()
    for _ in range(int(input())):
        c, *a = input().split()
        n = int(a[0])
        if c == 'I': s.add(n)
        elif c == 'D' and s:
            if n > 0: s.remove(s[-1])
            else: s.remove(s[0])
    if s:
        print(s[-1], s[0])
    else: print('EMPTY')