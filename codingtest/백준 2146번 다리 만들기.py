import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    res = int(1e9)
    sig = 0
    while ways:
        y, x = ways.pop(0)
        if dist[y][x] == sig: return res
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if not board[ny][nx]:
                    board[ny][nx] = board[y][x]
                    dist[ny][nx] = dist[y][x] + 1
                    ways.append((ny, nx))
                elif board[ny][nx] != board[y][x]:
                    sig = dist[y][x] + 1
                    if dist[ny][nx] == 0: return 1
                    if dist[ny][nx] < dist[y][x] + 1:
                        res = min(res, 2 * dist[ny][nx])
                    else: res = min(res, 2 * dist[y][x] + 1)

def main():
    global n, board, ways, dist
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    ways = []
    idx = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                q =[(i, j)]
                board[i][j] = idx
                while q:
                    y, x = q.pop(0)
                    for dy, dx in d:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            if board[ny][nx] == 1:
                                q.append((ny, nx))
                                board[ny][nx] = idx
                            elif not board[ny][nx]:
                                if dist[ny][nx]: continue
                                ways.append((ny, nx))
                                board[ny][nx] = idx
                                dist[ny][nx] = 1
                idx += 1
    print(bfs())

main()