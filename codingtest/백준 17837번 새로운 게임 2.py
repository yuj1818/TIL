import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def move(n, y, x, d):
    global isOver
    ny, nx = y + dy[d], x + dx[d]
    i = pos[y][x].index(n)
    if (not (0 <= ny < N and 0 <= nx < N)) or board[ny][nx] == 2:
        if d % 2: d -= 1
        else: d += 1
        ny, nx = y + dy[d], x + dx[d]
        info[n][2] = d
        if (not (0 <= ny < N and 0 <= nx < N)) or board[ny][nx] == 2: return
    if board[ny][nx] == 0:
        for idx in pos[y][x][i:]: pos[ny][nx].append(idx)
    if board[ny][nx] == 1:
        for idx in pos[y][x][i:][::-1]: pos[ny][nx].append(idx)
    for idx in pos[y][x][i:]:
        info[idx][0] = ny
        info[idx][1] = nx
    pos[y][x] = pos[y][x][:i]
    if len(pos[ny][nx]) >= 4:
        isOver = True
        return

def main():
    global N, board, pos, info, isOver
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    pos = [[[] for _ in range(N)] for _ in range(N)]
    info = []
    for i in range(K):
        y, x, d = map(lambda x: int(x) - 1, input().split())
        pos[y][x].append(i)
        info.append([y, x, d])
    ans = 0
    isOver = False
    while ans <= 1000:
        ans += 1
        for n in range(K):
            y, x, d = info[n]
            move(n, y, x, d)
            if isOver:
                print(ans)
                exit()
    print(-1)

main()