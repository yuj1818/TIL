T = int(input())
dx = [1, 0]
dy = [0, 1]

def dfs(y, x, sum_v):
    global min_v
    visited[y][x] = 1
    sum_v += board[y][x]
    if sum_v > min_v:
        return
    if x == N - 1 and y == N - 1:
        min_v = min(min_v, sum_v)
        return

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if x <= nx < N and y <= ny < N:
            if not visited[ny][nx]:
                dfs(ny, nx, sum_v)
                visited[ny][nx] = 0

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_v = sum(sum(row) for row in board)
    visited = [[0] * N for _ in range(N)]
    dfs(0, 0, 0)
    print(f'#{tc} {min_v}')