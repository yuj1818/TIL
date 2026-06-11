def move():
    for n in range(1, MAX + 1):
        y, x = pos[n]
        max_n = 0
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N): continue
            max_n = max(max_n, grid[ny][nx])
        my, mx = pos[max_n]
        grid[y][x] = max_n
        grid[my][mx] = n
        pos[n] = (my, mx)
        pos[max_n] = (y, x)

d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
N, M = map(int, input().split())
MAX = N ** 2
grid = [list(map(int, input().split())) for _ in range(N)]
pos = dict()
for i in range(N):
    for j in range(N):
        pos[grid[i][j]] = (i, j)
for _ in range(M):
    move()
for row in grid:
    print(' '.join(map(str, row)))