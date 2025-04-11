import sys
input = sys.stdin.readline

def init():
    dyx = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    limit, cnt, d, idx = 1, 0, 0, 1
    i, j = n // 2, n // 2
    while 1:
        dy, dx = dyx[d]
        for _ in range(limit):
            i += dy
            j += dx
            if (i, j) == (0, -1): return
            marbles.append(info[i][j])
            info[i][j] = idx
            idx += 1
        d = (d + 1) % 4
        cnt += 1
        if cnt == 2:
            limit += 1
            cnt = 0

def destroy(d, s):
    global marbles
    y = x = n // 2
    dy, dx = dyx[d]
    for _ in range(s):
        y += dy
        x += dx
        marbles[info[y][x]] = -1
    pull()

def pull():
    global marbles
    cnt = marbles.count(-1)
    marbles = [x for x in marbles if x != -1]
    marbles.extend([0] * cnt)

def connected():
    global ans
    sig, t, cnt, num = 0, 0, 0, 0
    for i in range(1, n ** 2):
        if marbles[i] == num:
            cnt += 1
        else:
            if cnt >= 4:
                sig = 1
                for j in range(t, i):
                    marbles[j] = -1
                ans += num * cnt
            cnt = 1
            t = i
            num = marbles[i]
    return sig

def trans():
    global marbles
    nmarbles = [0]
    num, cnt = 0, 0
    for i in range(1, n ** 2):
        if num == marbles[i]: cnt += 1
        else:
            if cnt: nmarbles.extend([cnt, num])
            num = marbles[i]
            cnt = 1
    for i in range(len(nmarbles)):
        if i >= n ** 2: break
        marbles[i] = nmarbles[i]

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
marbles = [0]
init()
ans = 0
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(m):
    d, s = map(int, input().split())
    destroy(d - 1, s)
    while 1:
        if not connected(): break
        pull()
    trans()
print(ans)