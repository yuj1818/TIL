import sys
input = sys.stdin.readline
d = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}
trans = lambda x: int(x) if x.isdigit() else [int(x[1]) - 1, ord(x[0]) - 65]
k, s, n = map(trans, input().rstrip().split())
ky, kx = k
sy, sx = s
for _ in range(n):
    dy, dx = d[input().rstrip()]
    nky, nkx = ky + dy, kx + dx
    if not (0 <= nky < 8 and 0 <= nkx < 8): continue
    if (nky, nkx) == (sy, sx):
        nsy, nsx = sy + dy, sx + dx
        if not (0 <= nsy < 8 and 0 <= nsx < 8): continue
        sy, sx = nsy, nsx
    ky, kx = nky, nkx
print(f'{chr(kx + 65)}{ky + 1}')
print(f'{chr(sx + 65)}{sy + 1}')