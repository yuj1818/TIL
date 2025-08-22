import sys
input = sys.stdin.readline
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    pos = []
    for i in range(n):
        for j in range(m):
            if board[i][j]: pos.append((i, j))
    ans = -1
    visited = [[0] * m for _ in range(n)]
    while pos:
        y, x = pos.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            nd = visited[y][x] + 1
            if 0 <= ny < n and 0 <= nx < m and not board[ny][nx] and not visited[ny][nx]:
                pos.append((ny, nx))
                visited[ny][nx] = nd
                if ans < nd: ans = nd
    print(ans)

main()