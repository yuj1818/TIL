d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, h, m = map(int, input().split())
p = []
board = []
for i in range(n):
    r = list(map(int, input().split()))
    for j in range(n):
        if r[j] == 2: p.append((i, j))
    board.append(r)
ans = [[0] * n for _ in range(n)]
for i in range(h):
    py, px = p[i]
    visited = [[0] * n for _ in range(n)]
    visited[py][px] = 1
    q = [(py, px, 0)]
    while q:
        y, x, cnt = q.pop(0)
        if board[y][x] == 3:
            ans[py][px] = cnt
            break
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] == 1 or visited[ny][nx]: continue
            q.append((ny, nx, cnt + 1))
            visited[ny][nx] = 1
    else: ans[py][px] = -1
for r in ans:
    print(' '.join(map(str, r)))
