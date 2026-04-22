def trans_b(c):
    if c == 'T': return 4
    if c == 'C': return 2
    if c == 'M': return 1

def make_group(sy, sx):
    q = [(sy, sx)]
    visited[sy][sx] = 1
    group = [[sy, sx]]
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not(0 <= ny < N and 0 <= nx < N) or visited[ny][nx]: continue
            if F[sy][sx] == F[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1
                group.append([ny, nx])
    group.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    ry, rx = group[0][0], group[0][1]
    for i in range(1, len(group)):
        B[ry][rx] += 1
        B[group[i][0]][group[i][1]] -= 1
    group.append(F[sy][sx])
    return group

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, T = map(int, input().split())
F = [list(map(trans_b, input())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    # 아침 시간
    for i in range(N):
        for j in range(N):
            B[i][j] += 1
    # 점심 시간
    visited = [[0] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            groups.append(make_group(i, j))
    # 저녁 시간
    groups.sort(key=lambda x: (bin(x[-1]).count('1'), -B[x[0][0]][x[0][1]], x[0][0], x[0][1]))
    limit = set()
    for group in groups:
        f = group[-1]
        ry, rx = group[0][0], group[0][1]
        if (ry, rx) in limit: continue
        x = B[ry][rx] - 1
        di = B[ry][rx] % 4
        B[ry][rx] = 1
        dy, dx = d[di]
        ny, nx = ry, rx
        while x > 0:
            ny += dy
            nx += dx
            if not (0 <= ny < N and 0 <= nx < N): break
            if F[ny][nx] == f: continue
            if B[ny][nx] < x:
                F[ny][nx] = f
                B[ny][nx] += 1
                x -= B[ny][nx]
            else:
                F[ny][nx] |= f
                B[ny][nx] += x
                x = 0
            limit.add((ny, nx))
    cnt = [0] * 8
    for i in range(N):
        for j in range(N):
            cnt[F[i][j]] += B[i][j]
    print(' '.join([str(cnt[x]) for x in [7, 6, 5, 3, 1, 2, 4]]))
