N, K = map(int, input().split())
l = [i for i in range(1, N + 1)]
print('<', end='')
while len(l) > 1:
    rmv_idx = (K - 1) % len(l)
    nl = l[rmv_idx + 1:] + l[:rmv_idx]
    print(l.pop(rmv_idx), end=', ')
    l = nl
print(f'{l.pop()}>')