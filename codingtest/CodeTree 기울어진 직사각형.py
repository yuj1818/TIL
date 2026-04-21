def calc(y, x, k, l):
    move = [k, l, k, l]
    total = 0
    for i in range(4):
        dy, dx = d[i]
        m = move[i]
        for _ in range(m):
            y, x = y + dy, x + dx
            if not (0 <= y < n and 0 <= x < n): return 0
            total += grid[y][x]
    return total

d = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(2, n):
    for j in range(1, n - 1):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, calc(i, j, k, l))
print(ans)
