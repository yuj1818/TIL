T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_exit(N):
    while stack:
        y, x = stack[-1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and maze[ny][nx] != '1' and not visited[ny][nx]:
                if maze[ny][nx] == '2':
                    return 1
                stack.append((ny, nx))
                visited[ny][nx] = 1
                break
        else:
            stack.pop()
    return 0


for tc in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    sig = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                stack = [(i, j)]
                visited[i][j] = 1
                sig = 1
                break
        if sig:
            break
    print(f'#{tc} {find_exit(N)}')