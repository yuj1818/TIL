import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
v = []
zero = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            v.append((i, j))
            visited[i][j] = 3
        elif board[i][j] == 0:
            zero += 1
        else:
            visited[i][j] = 1
ans = n * n if zero else 0

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(v):
    q = deque()
    cnt = zero
    virus = [visited[i][::] for i in range(n)]
    for y, x in v:
        virus[y][x] = 2
        q.append((y, x, 0))
    while q:
        y, x, t = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= nx < n and 0 <= ny < n and virus[ny][nx] != 1 and virus[ny][nx] != 2:
                if virus[ny][nx] == 0:
                    cnt -= 1
                virus[ny][nx] = 2
                q.append((ny, nx, t+1))
                if cnt == 0:
                    return t + 1 
    return n * n

for comb in combinations(v, m):
    if ans == 0: break
    ans = min(ans, bfs(comb))

print(ans if ans != n * n else -1)