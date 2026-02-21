n = list(map(int, input()))
if 0 not in n or sum(n) % 3:
    print(-1)
    exit()
print(''.join(map(str, sorted(n, reverse=True))))