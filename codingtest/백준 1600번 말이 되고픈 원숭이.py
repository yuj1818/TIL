import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
md = [(0, 1), (1, 0), (0, -1), (-1, 0)]
hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

def bfs():
    q = [(0, 0, k)]
    cnt = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    while q:
        y, x, kc = q.pop(0)
        if (y, x) == (h - 1, w - 1): return cnt[y][x][kc]
        if kc > 0:
            for dy, dx in hd:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not board[ny][nx] and not cnt[ny][nx][kc - 1]:
                    q.append((ny, nx, kc - 1))
                    cnt[ny][nx][kc - 1] = cnt[y][x][kc] + 1
        for dy, dx in md:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not board[ny][nx] and not cnt[ny][nx][kc]:
                q.append((ny, nx, kc))
                cnt[ny][nx][kc] = cnt[y][x][kc] + 1
    return -1

def main():
    global k, w, h, board
    k = int(input())
    w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    print(bfs())

main()