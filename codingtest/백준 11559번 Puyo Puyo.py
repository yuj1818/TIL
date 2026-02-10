import sys

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
game = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
ans = 0
while 1:
    bomb = []
    visited = [[0] * 6 for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if game[y][x] == '.' or visited[y][x]:
                continue
            visited[y][x] = 1
            s = [(y, x)]
            cnt, idx = 1, 0
            while idx < cnt:
                i, j = s[idx]
                idx += 1
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < 12
                        and 0 <= nj < 6
                        and not visited[ni][nj]
                        and game[ni][nj] == game[i][j]
                    ):
                        visited[ni][nj] = 1
                        s.append((ni, nj))
                        cnt += 1
            if cnt >= 4:
                bomb.extend(s)
    for y, x in bomb:
        game[y][x] = '.'
    puyo = [[] for _ in range(6)]
    for y in range(12):
        for x in range(6):
            if game[y][x] != '.':
                puyo[x].append(game[y][x])
    ngame = [['.'] * 6 for _ in range(12)]
    for x in range(6):
        for i in range(-len(puyo[x]), 0):
            ngame[i][x] = puyo[x][i]
    game = ngame
    if not bomb:
        break
    ans += 1
print(ans)
