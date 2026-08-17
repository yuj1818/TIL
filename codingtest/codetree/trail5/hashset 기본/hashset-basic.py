s = set()
for _ in range(int(input())):
    c, x = input().split()
    if c == 'add': s.add(x)
    elif c == 'remove': s.remove(x)
    else: print('true' if x in s else 'false')