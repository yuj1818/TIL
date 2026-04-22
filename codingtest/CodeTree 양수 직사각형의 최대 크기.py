def search(y1, x1):
    max_v = 0
    mw = m
    for y2 in range(y1, n):
        for x2 in range(x1, mw):
            if grid[y2][x2] <= 0:
                if x1 == x2: return max(max_v, (y2 - y1) * (mw - x1))
                max_v = max(max_v, (y2 - y1) * (mw - x1))
                mw = x2
                break
    return max(max_v, (n - y1) * (mw - x1))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_v = -1
for y in range(n):
    for x in range(m):
        if grid[y][x] <= 0: continue
        max_v = max(max_v, search(y, x))
print(max_v)
