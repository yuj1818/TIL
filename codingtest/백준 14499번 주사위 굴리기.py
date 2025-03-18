import sys
input = sys.stdin.readline
n, m, y, x, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
com = list(map(int, input().split()))
dyx = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0] * 6
rotate = [
    [3, 1, 0, 5, 4, 2],
    [2, 1, 5, 0, 4, 3],
    [4, 0, 2, 3, 5, 1],
    [1, 5, 2, 3, 0, 4]
]

for d in com:
    ny, nx = y + dyx[d][0], x + dyx[d][1]
    if 0 <= ny < n and 0 <= nx < m:
        y, x = ny, nx
        dice = [dice[i] for i in rotate[d - 1]]
        if grid[y][x] == 0: grid[y][x] = dice[-1]
        else:
            dice[-1] = grid[y][x]
            grid[y][x] = 0
        print(dice[0])