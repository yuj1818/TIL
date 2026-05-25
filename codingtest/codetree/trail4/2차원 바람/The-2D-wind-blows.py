import math

def move(r1, c1, r2, c2):
    w, h = c2 - c1, r2 - r1
    na = [row[:] for row in a]
    y, x = r1, c1
    for dy, dx in d:
        c = 0
        if dx: c = w
        else: c = h
        for _ in range(c):
            ny, nx = y + dy, x + dx
            na[ny][nx] = a[y][x]
            y, x = ny, nx
    return na

def calc(r1, c1, r2, c2):
    na = [row[:] for row in a]
    for y in range(r1, r2 + 1):
        for x in range(c1, c2 + 1):
            total, cnt = na[y][x], 1
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < n and 0 <= nx < m): continue
                total += a[ny][nx]
                cnt += 1
            na[y][x] = math.floor(total / cnt)
    return na

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for r1, c1, r2, c2 in [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]:
    a = move(r1, c1, r2, c2)
    a = calc(r1, c1, r2, c2)
for row in a:
    print(' '.join(map(str, row)))