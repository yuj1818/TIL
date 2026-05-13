d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = -1
q = [(0, 0, 0)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
while q:
    y, x, dist = q.pop(0)
    if y == n - 1 and x == m - 1:
        ans = dist
        break
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < m) or visited[ny][nx] or a[ny][nx] == 0: continue
        visited[ny][nx] = 1
        q.append((ny, nx, dist + 1))
print(ans)
