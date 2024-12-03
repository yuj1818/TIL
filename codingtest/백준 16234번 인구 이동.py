from collections import deque
import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def bfs(y, x):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[y][x] = 1
    q = deque([(y, x)])
    s = [(y, x)]
    total = countries[y][x]
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and l <= abs(countries[i][j] - countries[ni][nj]) <= r and not visited[ni][nj]:
                visited[ni][nj] = 1
                s.append((ni, nj))
                total += countries[ni][nj]
                q.append((ni, nj))
    v = total // len(s)
    for cy, cx in s:
        countries[cy][cx] = v

while True:
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt == n * n:
        break
    ans += 1

print(ans)