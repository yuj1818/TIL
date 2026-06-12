def move(obj):
    y, x, di = obj
    dy, dx = dyx[di]
    ny, nx = y + dy, x + dx
    if not (0 <= ny < N and 0 <= nx < N): return (y, x, (di + 2) % 4)
    grid[ny][nx] += 1
    grid[y][x] -= 1
    return (ny, nx, di)

T = int(input())
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(T):
    N, M = map(int, input().split())
    grid = [[0] * N for _ in range(N)]
    a = []
    for _ in range(M):
        y, x, d = input().split()
        y, x = int(y) - 1, int(x) - 1
        grid[y][x] = 1
        di = 0
        if d == 'U': di = 3
        elif d == 'D': di = 1
        elif d == 'L': di = 2
        a.append((y, x, di))
    for _ in range(2 * N):
        for i, obj in enumerate(a):
            a[i] = move(obj)
        na = []
        for y, x, di in a:
            if grid[y][x] == 1: na.append((y, x, di))
            elif grid[y][x] > 1: grid[y][x] = 0
        a = na
    print(len(a))
                