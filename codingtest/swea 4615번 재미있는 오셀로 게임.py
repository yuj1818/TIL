T = int(input())
dx = [0, 0, -1, 1, -1, 1, 1, -1] # 상 하 좌 우 좌상 우하 우상 좌하
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1:N // 2 + 1] = [2, 1]
    board[N // 2][N // 2 - 1:N // 2 + 1] = [1, 2]
    for _ in range(M):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        board[y][x] = c
        for d in range(8):
            stack = []
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < N and 0 <= ny < N and board[ny][nx]:
                if board[ny][nx] == c:
                    for i, j in stack:
                        board[i][j] = c
                    break
                stack.append((ny, nx))
                nx += dx[d]
                ny += dy[d]
    print(f'#{tc} {sum([row.count(1) for row in board])} {sum([row.count(2) for row in board])}')