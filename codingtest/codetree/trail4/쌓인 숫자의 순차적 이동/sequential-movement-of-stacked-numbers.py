def move(y, x, idx):
    moved = 0
    my, mx, mnum = -1, -1, -1
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n) or len(current[ny][nx]) == 0: continue
        moved = 1
        mv = max(current[ny][nx])
        if mnum < mv: my, mx, mnum = ny, nx, mv
    if not moved: return
    for i in range(idx, len(current[y][x])):
        pos[current[y][x][i]] = [my, mx]
        current[my][mx].append(current[y][x][i])
    current[y][x] = current[y][x][:idx]

d = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
current = [[[] for _ in range(n)] for _ in range(n)]
pos = [[0, 0] for _ in range(n ** 2 + 1)]
for i in range(n):
    for j in range(n):
        current[i][j].append(grid[i][j])
        pos[grid[i][j]] = [i, j]

for num in list(map(int, input().split())):
    y, x = pos[num]
    idx = current[y][x].index(num)
    move(y, x, idx)

for i in range(n):
    for j in range(n):
        if current[i][j]: print(' '.join(map(str, current[i][j][::-1])))
        else: print('None')