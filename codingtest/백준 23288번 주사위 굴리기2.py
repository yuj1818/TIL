import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dice = [1, 2, 3, 4, 5, 6]
y, x = 0, 0
roll = [
    [3, 1, 0, 5, 4, 2],
    [1, 5, 2, 3, 0, 4],
    [2, 1, 5, 0, 4, 3],
    [4, 0, 2, 3, 5, 1]
]
scores = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if scores[i][j] == 0:
            scores[i][j] = 1
            s = [(i, j)]
            tmp = [(i, j)]
            while s:
                cy, cx = s.pop()
                for dy, dx in d:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < m and not scores[ny][nx] and grid[ny][nx] == grid[i][j]:
                        s.append((ny, nx))
                        tmp.append((ny, nx))
                        scores[ny][nx] = 1
            score = grid[i][j] * len(tmp)
            for ti, tj in tmp:
                scores[ti][tj] = score

di, ans = 0, 0
while k > 0:
    dy, dx = d[di]
    ny, nx = y + dy, x + dx
    if 0 <= ny < n and 0 <= nx < m:
        k -= 1
        dice = [dice[i] for i in roll[di]]
        y, x = ny, nx
        ans += scores[y][x]
        if dice[-1] == grid[y][x]: continue
        elif dice[-1] > grid[y][x]: di = (di + 1) % 4
        else: di = (di - 1) % 4
    else:
        di = (di + 2) % 4

print(ans)