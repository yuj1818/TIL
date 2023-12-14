from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
MAP = []
visited = [[0] * m for _ in range(n)]
sy, sx = 0, 0
ans = 0

for i in range(n):
    line = list(input())
    for j in range(m):
        if line[j] == 'I':
            sy, sx = i, j
    MAP.append(line)

q = deque([(sy, sx)])
visited[sy][sx] = 1
while q:
    y, x = q.popleft()

    for i in range(4):
       ny, nx = y + dy[i], x + dx[i]

       if 0 <= ny < n and 0 <= nx < m and MAP[ny][nx] != 'X' and not visited[ny][nx]:
           q.append((ny, nx))
           visited[ny][nx] = 1

           if MAP[ny][nx] == 'P':
               ans += 1

print(ans if ans else 'TT')