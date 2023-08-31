from collections import deque
T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def calc_dist(y, x):
    global max_dist, max_r_n
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((y, x))
    visited[y][x] = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and rooms[r][c] + 1 == rooms[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    if (y, x) != (r, c):
        if max_dist == visited[r][c]:
            max_r_n = rooms[y][x] if rooms[y][x] < max_r_n else max_r_n
        elif max_dist < visited[r][c]:
            max_dist = visited[r][c]
            max_r_n = rooms[y][x]

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    max_dist = 1
    max_r_n = N ** 2
    for i in range(N):
        for j in range(N):
            calc_dist(i, j)
    print(f'#{tc} {max_r_n} {max_dist}')