import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    heights = [[] for _ in range(501)]
    for i in range(n):
        for j in range(m):
            heights[board[i][j]].append((i, j))
    visited = [[0] * m for _ in range(n)]
    ans = 0
    for h in range(500, -1, -1):
        for y, x in heights[h]:
            if visited[y][x]: continue
            ans += 1
            s = [(y, x)]
            visited[y][x] = 1
            while s:
                y, x = s.pop()
                for dy, dx in d:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if visited[ny][nx] or board[ny][nx] > board[y][x]: continue
                        visited[ny][nx] = 1
                        s.append((ny, nx))
    print(ans)

main()