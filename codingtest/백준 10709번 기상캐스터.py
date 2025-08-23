import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sky = [input().strip() for _ in range(n)]
q = []
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if sky[i][j] == 'c':
            q.append((i, j))
            visited[i][j] = 0
while q:
    y, x = q.pop(0)
    if 0 <= x + 1 < m and visited[y][x + 1] == -1:
        q.append((y, x + 1))
        visited[y][x + 1] = visited[y][x] + 1
print('\n'.join(map(lambda x: ' '.join(map(str, x)), visited)))