from collections import deque
T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x, y):
    q = deque()
    if not visited[y][x]:
        visited[y][x] = 1
        q.append((y, x))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and farm[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [list(map(int, input().split())) for _ in range(K)]
    farm = [[0] * M for _ in range(N)]
    for cabbage in cabbages:
        farm[cabbage[1]][cabbage[0]] = 1
    visited = [[0] * M for _ in range(N)]
    ans = 0
    for cabbage in cabbages:
        x, y = cabbage
        if not visited[y][x]:
            bfs(x, y)
            ans += 1
    print(ans)