N, M = map(int, input().split())
board = [input() for _ in range(N)]
case = ['WBWBWBWB', 'BWBWBWBW'] * 4
start_x = 0
start_y = 0
answer = 64
while start_y + 8 <= N:
    cy = 0
    cnt = 0
    for i in range(start_y, start_y + 8):
        cx = 0
        for j in range(start_x, start_x + 8):
            if case[cy][cx] != board[i][j]:
                cnt += 1
            cx += 1
        cy += 1
    answer = min(answer, cnt, 64 - cnt)

    if start_x < (M - 8):
        start_x += 1
    else:
        start_x = 0
        start_y += 1

print(answer)