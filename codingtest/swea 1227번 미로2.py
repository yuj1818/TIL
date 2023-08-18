N = 100
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x, N):
    q = []
    visited = [[0] * N for _ in range(N)]
    q.append((y, x))
    visited[y][x] = 1
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nc < N and 0 <= nr < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 0

for _ in range(1, 11):
    tc = int(input())
    maze = []
    found_s = False
    for i in range(N):
        line = list(map(int, input()))
        if not found_s:
            for j in range(N):
                if line[j] == 2:
                    y, x = i, j
                    found_s = True
                    break
        maze.append(line)
    print(f'#{tc} {bfs(y, x, N)}')
