import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
home = [list(map(int, input().decode().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x):
    global num

    visited[y][x] = 1
    num += 1

    for dy, dx in d:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and home[ny][nx]:
            dfs(ny, nx)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and home[i][j]:
            num = 0
            dfs(i, j)
            ans.append(num)

print(len(ans))
for x in sorted(ans):
    print(x)