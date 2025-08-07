import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move_water():
    q = []
    for wy, wx in water:
        time[wy][wx] = 0
        q.append((wy, wx))
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'X' and (ny, nx) != (ey, ex) and time[ny][nx] > time[y][x] + 1:
                q.append((ny, nx))
                time[ny][nx] = time[y][x] + 1

def move():
    visited = [[0] * c for _ in range(r)]
    visited[sy][sx] = 1
    q = [(sy, sx, 0)]
    while q:
        y, x, cnt = q.pop(0)
        if y == ey and x == ex: return cnt
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'X' and time[ny][nx] > cnt + 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, cnt + 1))
    return 'KAKTUS'

r, c = map(int, input().split())
board = []
ey, ex, sy, sx = 0, 0, 0, 0
water = []
for i in range(r):
    row = input().strip()
    for j in range(c):
        if row[j] == 'D': ey, ex = i, j
        elif row[j] == 'S': sy, sx = i, j
        elif row[j] == '*': water.append((i, j))
    board.append(row)
time = [[float('inf')] * c for _ in range(r)]
move_water()
print(move())