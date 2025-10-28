import sys
input = sys.stdin.readline

def main():
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    q = [(0, 0)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x = q.pop(0)
        if y == n - 1 and x == m - 1: return 'Yes'
        for dy, dx in [(0, 1), (1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))
    return 'No'

print(main())