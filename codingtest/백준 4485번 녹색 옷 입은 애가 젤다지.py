def bfs(y, x):
    q = []
    heapq.heappush(q, (cave[y][x], y, x))
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    while q:
        w, y, x = heapq.heappop(q)
        if x == n - 1 and y == n - 1: return w
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = 1
                heapq.heappush(q, (w + cave[ny][nx], ny, nx))

import sys, heapq
input = sys.stdin.readline
tc = 1
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while True:
    n = int(input())
    if n == 0: break
    cave = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {tc}: {bfs(0, 0)}')
    tc += 1