import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x):
    s = 1
    paint[y][x] = 0
    stk = [(y, x)]
    while stk:
        y, x = stk.pop()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and paint[ny][nx]:
                s += 1
                stk.append((ny, nx))
                paint[ny][nx] = 0
    return s

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
cnt, size = 0, 0
for i in range(n):
    for j in range(m):
        if paint[i][j]:
            cnt += 1
            size = max(size, dfs(i, j))
print(f'{cnt}\n{size}')