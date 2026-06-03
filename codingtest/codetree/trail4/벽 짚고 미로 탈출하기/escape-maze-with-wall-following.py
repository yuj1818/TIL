N = int(input())
y, x = map(lambda x: int(x) - 1, input().split())
grid = [list(input()) for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
di, t = 0, 0
s = [(y, x)]
visited = [[[0] * N for _ in range(N)] for _ in range(4)]
while s:
    y, x = s.pop()
    visited[di][y][x] = 1
    dy, dx = d[di]
    ny, nx = y + dy, x + dx
    if not (0 <= ny < N and 0 <= nx < N): 
        t += 1
        break
    if grid[ny][nx] == '#':
        di = (di - 1) % 4
        if visited[di][y][x]:
            t = -1
            break
        s.append((y, x))
        continue
    ndy, ndx = d[(di + 1) % 4]
    if grid[ny + ndy][nx + ndx] == '.':
        di = (di + 1) % 4
    if visited[di][ny][nx]:
        t = -1
        break
    s.append((ny, nx))
    t += 1
print(t)