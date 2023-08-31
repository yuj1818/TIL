from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    global min_v
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((y, x))
    visited[y][x] = 1
    while q:
        r, c = q.popleft()
        if r == N - 1 and c == M - 1:
            min_v = min(min_v, visited[r][c])

        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
min_v = N * M
bfs(0, 0)
print(min_v)