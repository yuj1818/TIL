T = int(input())
dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]

def bfs(y, x, N):
    q = []
    visited[y][x] = 1
    q.append((y, x))
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 2:
            return visited[r][c] - 2
        for d in range(4):
            nx = c + dx[d]
            ny = r + dy[d]
            if 0 <= nx < N and 0 <= ny < N and maze[ny][nx] != 1 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[r][c] + 1
    return 0

for tc in range(1, T + 1):
    N = int(input())
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    maze = []
    for i in range(N):
        line = list(map(int, input()))
        for j in range(N):
            if line[j] == 3:
                y, x = i, j
                break
        maze.append(line)
    print(f'#{tc} {bfs(y, x, N)}')