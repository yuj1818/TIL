from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()
for _ in range(n):
    c, *a = input().split()
    a = list(map(int, a))
    if c == 'add': 
        k, v = a
        sd[k] = v
    elif c == 'remove':sd.pop(a[0])
    elif c == 'find': print(sd.get(a[0], 'None'))
    else:
        if sd: print(' '.join(map(str, sd.values())))
        else: print('None')