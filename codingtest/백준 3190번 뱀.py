N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1
L = int(input())
play_time = 0
x = 0
y = 0
dx = 1
dy = 0
cnt = 0
for _ in range(L):
    s, r = input().split()
    for _ in range(int(s)):
        nx = x + 1 * dx
        ny = y + 1 * dy
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
            for ax, ay in apples:
                if nx == ax and ny == ay:
                    break
            else:
                board[y][x] = 0
            x = nx
            y = ny
            board[y][x] = 1
            cnt += 1
        else:
            break

    if dy == 0 and r == 'L':
        dx, dy = dy, -1 * dx
    elif dx == 0 and r == 'D':
        dx, dy = -1 * dy, dx
    else:
        dx, dy = dy, dx

print(cnt)

