d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s = [(r - 1, c - 1)]
while s:
    y, x = s.pop()
    print(grid[y][x], end=' ')
    ny, nx = y, x
    for dy, dx in d:
        cy, cx = y + dy, x + dx
        if not (0 <= cy < n and 0 <= cx < n) or grid[ny][nx] >= grid[cy][cx]: continue
        s.append((cy, cx))
        break