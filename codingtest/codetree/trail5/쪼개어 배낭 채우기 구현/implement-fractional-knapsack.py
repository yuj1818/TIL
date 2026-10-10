n, m = map(int, input().split())
jewels = []
for _ in range(n):
    w, v = map(int, input().split())
    jewels.append((w, v, v/w))
jewels.sort(key=lambda x: -x[2])
cw, cv = 0, 0
for w, v, vpw in jewels:
    if cw + w > m:
        r = m - cw
        cw += r
        cv += r * vpw
    else:
        cw += w
        cv += v
print(f'{cv:.3f}')