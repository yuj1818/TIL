import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
purifier = []
for i in range(r):
    if room[i][0] == -1: purifier.append(i)

def diffusion(room):
    nroom = [room[i][::] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                nroom[i][j] -= room[i][j]
                dd = room[i][j] // 5
                t = room[i][j]
                if i > 0 and room[i - 1][j] != -1:
                    t -= dd
                    nroom[i - 1][j] += dd
                if i + 1 < r and room[i + 1][j] != -1:
                    t -= dd
                    nroom[i + 1][j] += dd
                if j > 0 and room[i][j - 1] != -1:
                    t -= dd
                    nroom[i][j - 1] += dd
                if j + 1 < c and room[i][j + 1] != -1:
                    t -= dd
                    nroom[i][j + 1] += dd
                nroom[i][j] += t
    return nroom

def purify(pi):
    y, x, pre = purifier[pi], 0, 0
    if pi:
        d = [(0, 1, c - 1), (1, 0, r - y - 1), (0, -1, c - 1), (-1, 0, r - y - 2)]
    else:
        d = [(0, 1, c - 1), (-1, 0, y), (0, -1, c - 1), (1, 0, y - 1)]
    for dy, dx, cnt in d:
        for _ in range(cnt):
            ny, nx = y + dy, x + dx
            npre = room[ny][nx]
            room[ny][nx] = pre
            pre = npre
            y, x = ny, nx

for _ in range(t):
    room = diffusion(room)
    purify(0)
    purify(1)

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            ans += room[i][j]
print(ans)