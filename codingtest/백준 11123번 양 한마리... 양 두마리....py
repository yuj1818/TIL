import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#' and not visited[i][j]:
                ans += 1
                q = [(i, j)]
                visited[i][j] = 1
                while q:
                    y, x = q.pop(0)
                    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '#' and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            q.append((ny, nx))
    print(ans)