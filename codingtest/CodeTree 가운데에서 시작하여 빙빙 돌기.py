def draw():
    y, x, v, di, l, cnt = n // 2, n // 2, 2, 0, 1, 0
    a[y][x] = 1
    while v <= n ** 2:
        if cnt == 2:
            cnt = 0
            l += 1
        dy, dx = d[di]
        for _ in range(l):
            y += dy
            x += dx
            if not (0 <= y < n and 0 <= x < n): return
            a[y][x] = v
            v += 1
        cnt += 1
        di = (di + 1) % 4

d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
n = int(input())
a = [[0] * n for _ in range(n)]
draw()
for r in a: print(' '.join(map(str, r)))
