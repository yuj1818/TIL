import sys
input = sys.stdin.readline
N, H, W = map(int, input().split())
L = [input().rstrip() for _ in range(H)]
ans = ['?'] * N
for x in range(N * W):
    if ans[x // W] != '?': continue
    v, h = '', ''
    for y in range(H):
        if not v and L[y][x] != '?': v = L[y][x]
        if h or x % W: continue
        for nx in range(x, x + W):
            if L[y][nx] == '?': continue
            h = L[y][nx]
    ans[x // W] = v or h or '?'
print(''.join(map(str, ans)))