def go(i, j, di):
    t = 1
    y, x = i, j
    while 1:
        t += 1
        dy, dx = d[di]
        if grid[y][x] == 1:
            if dy == 0: di = (di - 1) % 4
            else: di = (di + 1) % 4
        elif grid[y][x] == 2:
            if dy == 0: di = (di + 1) % 4
            else: di = (di - 1) % 4
        dy, dx = d[di]
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n): return t
        y, x = ny, nx

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for j in range(n):
    ans = max(ans, go(0, j, 1), go(n - 1, j, 3))
for i in range(n):
    ans = max(ans, go(i, 0, 0), go(i, n - 1, 2))
print(ans)