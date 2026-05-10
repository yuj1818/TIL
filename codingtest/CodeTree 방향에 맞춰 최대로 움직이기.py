def go(y, x, cnt):
    global ans
    dy, dx = d[move_dir[y][x]]
    ny, nx = y, x
    isMoved = False
    while 1:
        ny += dy
        nx += dx
        if not (0 <= ny < n and 0 <= nx < n): break
        if num[ny][nx] <= num[y][x]: continue
        isMoved = True
        go(ny, nx, cnt + 1)
    if not isMoved and ans < cnt: ans = cnt

d = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
ans = 0
go(r - 1, c - 1, 0)
print(ans)
