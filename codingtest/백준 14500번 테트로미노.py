import sys
input = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = 0
maxV = max([max(line) for line in paper])

def find(y, x, cnt, total):
    global ans

    if cnt == 4:
        ans = max(ans, total)
        return

    if ans > total + maxV * (4 - cnt):
        return

    for dy, dx in d:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = 1
                find(y, x, cnt + 1, total + paper[ny][nx])
                visited[ny][nx] = 0

            visited[ny][nx] = 1
            find(ny, nx, cnt + 1, total + paper[ny][nx])
            visited[ny][nx] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        find(i, j, 1, paper[i][j])
        visited[i][j] = 0

print(ans)