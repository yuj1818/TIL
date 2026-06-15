from collections import defaultdict

def move(idx, y, x, v, di):
    cy, cx, cdi = y, x, di
    for _ in range(v):
        dy, dx = dyx[cdi]
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < N and 0 <= nx < N):
            cdi = (cdi + 2) % 4
            dy, dx = dyx[cdi]
            ny, nx = cy + dy, cx + dx
        cy, cx = ny, nx
    marbles[idx] = (cy, cx, v, cdi)

d_map = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M, T, K = map(int, input().split())
marbles = [0] * M
for i in range(M):
    r, c, d, v = input().split()
    marbles[i] = (int(r) - 1, int(c) - 1, int(v), d_map[d])
for _ in range(T):
    for i in range(M):
        if marbles[i]: move(i, *marbles[i])
    counter = defaultdict(list)
    for i in range(M):
        if marbles[i]:
            y, x, v, d = marbles[i]
            counter[(y, x)].append((v, i))
    for k in counter.keys():
        l = len(counter[k])
        if l > K:
            counter[k] = sorted(counter[k], reverse=True)
            for _ in range(l - K):
                v, i = counter[k].pop()
                marbles[i] = 0
ans = 0
for marble in marbles:
    if marble: ans += 1
print(ans)
            



