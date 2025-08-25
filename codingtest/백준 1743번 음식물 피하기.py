import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y, x):
    q = [(y, x, 1)]
    s = 1
    while q:
        y, x, c = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, c + 1))
                s += 1
    return s

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
arr = []
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1
    arr.append((y - 1, x - 1))
visited = [[0] * m for _ in range(n)]
ans = 0
for y, x in arr:
    if not visited[y][x]:
        visited[y][x] = 1
        res = bfs(y, x)
        if res > ans: ans = res
print(ans)