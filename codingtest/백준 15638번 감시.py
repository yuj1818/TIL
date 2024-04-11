from itertools import chain

N, M = map(int, input().split())
board = []
cctv = []
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
mode = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}
min_v = N * M

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] in [1, 2, 3, 4, 5]:
            cctv.append((line[j], i, j))
    board.append(line)

def dfs(depth, board):
    global min_v
    if depth == len(cctv):
        min_v = min(list(chain(*board)).count(0), min_v)
        return

    kind, y, x = cctv[depth]
    temp = [row[:] for row in board]
    for dirs in mode[kind]:
        for direction in dirs:
            nx = x
            ny = y
            while True:
                nx += d[direction][1]
                ny += d[direction][0]
                if 0 <= nx < M and 0 <= ny < N and temp[ny][nx] != 6:
                    if temp[ny][nx] == 0:
                        temp[ny][nx] = -1
                else: break
        dfs(depth + 1, temp)
        temp = [row[:] for row in board]

dfs(0, board)
print(min_v)
