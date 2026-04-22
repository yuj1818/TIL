import sys

def check(y1, x1, y2, x2, r1, c1, r2, c2):
    visited = [[0] * m for _ in range(n)]
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            visited[i][j] = 1
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if visited[i][j] == 1: return True
    return False

def find(y1, x1, y2, x2):
    global max_v
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if check(y1, x1, y2, x2, i, j, k, l): continue
                    s1 = acc[y2][x2] - (acc[y2][x1 - 1] if x1 > 0 else 0) - (acc[y1 - 1][x2] if y1 > 0 else 0) + (acc[y1 - 1][x1 - 1] if y1 > 0 and x1 > 0 else 0)
                    s2 = acc[k][l] - (acc[k][j - 1] if j > 0 else 0) - (acc[i - 1][l] if i > 0 else 0) + (acc[i - 1][j - 1] if i > 0 and j > 0 else 0)
                    if max_v < s1 + s2: max_v = s1 + s2

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * m for _ in range(n)]
for i in range(0, n):
    acc[i][0] = acc[i - 1][0] + grid[i][0]
    for j in range(1, m):
        if i == 0: acc[i][j] = acc[i][j - 1] + grid[i][j]
        else: acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + grid[i][j]
max_v = -sys.maxsize
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m): find(i, j, k, l)
print(max_v)
