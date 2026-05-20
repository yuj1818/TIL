def bfs(i, j):
    visited[i][j] = 1
    q = [(i, j)]
    t, cnt = grid[i][j], 1
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or grid[ny][nx] != t or visited[ny][nx]: continue
            cnt += 1
            visited[ny][nx] = 1
            q.append((ny, nx))
    return cnt

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans, m_size = 0, 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = bfs(i, j)
            if size >= 4:
                ans += 1
            if m_size < size: m_size = size
print(ans, m_size)