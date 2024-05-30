import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(2500)

n = int(input())
picture = [input().decode() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
c, cb = 0, 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x):
    global c

    visited[y][x] = 1

    for d in range(4):
        ny = direction[d][0] + y
        nx = direction[d][1] + x

        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and picture[ny][nx] == picture[y][x]:
            dfs(ny, nx)

for case in range(2):
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j)
                if case:
                    cb += 1
                else:
                    c += 1
    visited = [[0] * n for _ in range(n)]
    picture = [line.replace('G', 'R') for line in picture]

print(c, cb)