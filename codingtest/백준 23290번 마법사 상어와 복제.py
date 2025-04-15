import sys
input = sys.stdin.readline
trans = lambda x: int(x) - 1

def move(sy, sx, t):
    nfishes = dict()
    for pos, d_cnt in fishes.items():
        y, x = pos
        for d, cnt in d_cnt.items():
            for _ in range(8):
                dy, dx = fd[d]
                ny, nx = y + dy, x + dx
                if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != (sy, sx) and (board[ny][nx] == 0 or board[ny][nx] < t - 2): break
                d = (d - 1) % 8
            else:
                if not nfishes.get(pos): nfishes[pos] = {d: cnt}
                else:
                    if nfishes[pos].get(d): nfishes[pos][d] += cnt
                    else: nfishes[pos][d] = cnt
                continue
            if not nfishes.get((ny, nx)): nfishes[(ny, nx)] = {d: cnt}
            else:
                if nfishes[(ny, nx)].get(d): nfishes[(ny, nx)][d] += cnt
                else: nfishes[(ny, nx)][d] = cnt
    return nfishes

def make_path(sy, sx):
    paths = []
    for aidx, (ady, adx) in enumerate(sd):
        acnt = 0
        nay, nax = sy + ady, sx + adx
        if 0 <= nay < 4 and 0 <= nax < 4:
            acnt += sum(nfishes.get((nay, nax), {}).values())
        else: continue
        for bidx, (bdy, bdx) in enumerate(sd):
            bcnt = acnt
            nby, nbx = nay + bdy, nax + bdx
            if 0 <= nby < 4 and 0 <= nbx < 4:
                bcnt += sum(nfishes.get((nby, nbx), {}).values())
            else: continue
            for cidx, (cdy, cdx) in enumerate(sd):
                ccnt = bcnt
                ncy, ncx = nby + cdy, nbx + cdx
                if 0 <= ncy < 4 and 0 <= ncx < 4:
                    if nay != ncy or nax != ncx:
                        ccnt += sum(nfishes.get((ncy, ncx), {}).values())
                else: continue
                paths.append((ccnt, aidx, bidx, cidx))
    paths.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    return paths[0]

def main():
    global fd, sd, board, fishes, nfishes
    m, s = map(int, input().split())
    fd = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    sd = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    board = [[0] * 4 for _ in range(4)]
    fishes = dict()
    for _ in range(m):
        y, x, d = map(trans, input().split())
        if not fishes.get((y, x)): fishes[(y, x)] = {d: 1}
        else:
            if fishes[(y, x)].get(d): fishes[(y, x)][d] += 1
            else: fishes[(y, x)][d] = 1
    sy, sx = map(trans, input().split())
    for t in range(1, s + 1):
        nfishes = move(sy, sx, t)
        path = make_path(sy, sx)
        for i in range(1, 4):
            dy, dx = sd[path[i]]
            sy += dy
            sx += dx
            if nfishes.get((sy, sx)) and sum(nfishes.get((sy, sx)).values()) > 0:
                nfishes[(sy, sx)].clear()
                board[sy][sx] = t
        for pos, d_cnt in nfishes.items():
            if not fishes.get(pos): fishes[pos] = d_cnt
            else:
                for d, cnt in d_cnt.items():
                    if fishes[pos].get(d): fishes[pos][d] += cnt
                    else: fishes[pos][d] = cnt

    print(sum([sum(d_cnt.values()) for d_cnt in fishes.values()]))

main()