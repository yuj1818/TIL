from collections import deque
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
input = open(0).readline
while 1:
    def bfs(s):
        visited = [[0] * w for _ in range(h)]
        res = [0] * cd
        sy, sx = s
        q = deque([(sy, sx, 0)])
        visited[sy][sx] = 1
        res[di[s]] = 0
        cnt = 1

        while q:
            y, x, c = q.popleft()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and room[ny][nx] != 'x' and not visited[ny][nx]:
                    if (ny, nx) in di:
                        res[di[(ny, nx)]] = c + 1
                        cnt += 1
                    visited[ny][nx] = 1
                    q.append((ny, nx, c + 1))

        if cnt != cd: return False
        return res

    def dfs(s, visited):
        if visited == (1 << cd) - 1:
            return 0

        if tsp[s][visited] != int(1e9): return tsp[s][visited]

        for i in range(1, cd):
            if visited & (1 << i): continue
            tsp[s][visited] = min(tsp[s][visited], dfs(i, visited | (1 << i)) + dist[s][i])

        return tsp[s][visited]

    w, h = map(int, input().split())
    if w + h == 0: break
    room = []
    dirt = []
    for i in range(h):
        row = list(input().strip())
        for j in range(w):
            if row[j] == 'o':
                dirt.insert(0, (i, j))
            elif row[j] == '*':
                dirt.append((i, j))
        room.append(row)
    di = {}
    for idx, pos in enumerate(dirt):
        di[pos] = idx
    cd = len(dirt)
    dist = []
    sig = 0
    for i in range(cd):
        visited = bfs(dirt[i])
        if visited:
            dist.append(visited)
        else:
            sig = 1
            break

    if sig:
        print(-1)
        continue

    tsp = [[int(1e9)] * (1 << cd) for _ in range(cd)]
    print(dfs(0, 1)) 