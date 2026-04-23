n = int(input())
grid = [input() for _ in range(n)]
k = int(input()) - 1
di = k // n
idx = k % n
if di > 1: idx = n + (idx * -1 - 1)
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
ans = 0
if di % 2:
    y = idx
    x = n if di == 1 else -1
else:
    x = idx
    y = n if di == 2 else -1
while 1:
    dy, dx = d[di]
    y += dy
    x += dx
    if not (0 <= y < n and 0 <= x < n): break
    ans += 1
    m = grid[y][x]
    if di % 2:
        if m == '/': di = (di - 1) % 4
        else: di = (di + 1) % 4
    else:
        if m == '/': di = (di + 1) % 4
        else: di = (di - 1) % 4
print(ans)
