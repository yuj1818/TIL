import sys
input = sys.stdin.readline

def bfs():
    q = [(r1, c1, 0)]
    visited = [[0] * n for _ in range(n)]
    visited[r1][c1] = 1
    while q:
        y, x, cnt = q.pop(0)
        if y == r2 and x == c2: return cnt
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                q.append((ny, nx, cnt + 1))
                visited[ny][nx] = 1
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
print(bfs())