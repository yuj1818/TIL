d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
n = int(input())
sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
visited = [[0] * n for _ in range(n)]
visited[sy][sx] = 1
q = [(sy, sx, 0)]
ans = -1
while q:
    y, x, cnt = q.pop(0)
    if y == ey and x == ex:
        ans = cnt
        break
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n) or visited[ny][nx]: continue
        visited[ny][nx] = 1
        q.append((ny, nx, cnt + 1))
print(ans)
