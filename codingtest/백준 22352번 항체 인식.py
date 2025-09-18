import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j, num):
    q = [(i, j)]
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    target = before[i][j]
    while q:
        y, x = q.pop(0)
        before[y][x] = num
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if before[ny][nx] == target:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

def check():
    for i in range(n):
        for j in range(m):
            if after[i][j] == before[i][j]: continue
            else: return False
    return True

def solve():
    for i in range(n):
        for j in range(n):
            if before[i][j] != after[i][j]:
                bfs(i, j, after[i][j])
                if check(): return 'YES'
                else: return 'NO'
    return 'YES'

print(solve())