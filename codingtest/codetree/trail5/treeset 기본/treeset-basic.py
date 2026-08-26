from sortedcontainers import SortedSet
n = int(input())
s = SortedSet()
for _ in range(n):
    c, *x = input().split()
    if c == 'largest':
        print(s[-1] if s else 'None')
    elif c == 'smallest':
        print(s[0] if s else 'None')
    else:
        x = int(x[0])
        if c == 'add':
            s.add(x)
        elif c == 'remove':
            s.remove(x)
        elif c == 'find':
            print('true' if x in s else 'false')
        elif c == 'lower_bound':
            idx = s.bisect_left(x)
            print(s[idx] if idx < len(s) else 'None')
        else: 
            idx = s.bisect_right(x)
            print(s[idx] if idx < len(s) else 'None')