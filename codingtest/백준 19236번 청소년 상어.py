import sys
input = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

def move(board, fish):
    for fn in range(1, 17):
        if not fish.get(fn): continue
        i, j, d = fish[fn]
        while i + dy[d] < 0 or i + dy[d] >= 4 or j + dx[d] < 0 or j + dx[d] >= 4 or board[i + dy[d]][j + dx[d]] == 17:
            d = (d + 1) % 8
        ni, nj = i + dy[d], j + dx[d]
        if board[ni][nj] == 0:
            board[i][j] = 0
            board[ni][nj] = fn
            fish[fn] = (ni, nj, d)
        else:
            tfn = board[ni][nj]
            tfd = fish[tfn][-1]
            board[ni][nj] = fn
            fish[fn] = (ni, nj, d)
            board[i][j] = tfn
            fish[tfn] = (i, j, tfd)
    return board, fish

def shark(i, j, cnt, fish, board):
    global ans
    nboard = [board[i][::] for i in range(4)]
    nfish = {k: v for k, v in fish.items()}
    fn = nboard[i][j]
    d = nfish[fn][-1]
    cnt += fn
    nboard[i][j] = 17
    nfish.pop(fn)
    nboard, nfish = move(nboard, nfish)
    sig = 0
    nboard[i][j] = 0
    while 0 <= i + dy[d] < 4 and 0 <= j + dx[d] < 4:
        i += dy[d]
        j += dx[d]
        if nboard[i][j] != 0:
            sig = 1
            shark(i, j, cnt, nfish, nboard)
    if not sig:
        if cnt > ans: ans = cnt

board = [[0] * 4 for _ in range(4)]
fish = dict()
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        fish[row[j * 2]] = (i, j, row[j * 2 + 1] - 1)
        board[i][j] = row[j * 2]
ans = 0
shark(0, 0, 0, fish, board)
print(ans)