import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0)]

def bfs():
    q = [(0, 0)]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x = q.pop(0)
        if board[y][x] == -1: return True
        dist = board[y][x]
        for dy, dx in d:
            ny, nx = y + dy * dist, x + dx * dist
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1
    return False

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print('HaruHaru' if bfs() else 'Hing')