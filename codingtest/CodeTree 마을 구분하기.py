def dfs(y, x):
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n) or not grid[ny][nx] or visited[ny][nx]: continue
        visited[ny][nx] = 1
        group[-1] += 1
        dfs(ny, nx)

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
group = []
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = 1
            group.append(1)
            dfs(i, j)
group.sort()
print(len(group))
print('\n'.join(map(str, group)))
