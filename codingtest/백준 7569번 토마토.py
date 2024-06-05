import sys
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n, h = map(int, input().split())
boxes = []
complete = 0
total = m * n * h
q = []
day = 0
for k in range(h):
    box = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 1:
                complete += 1
                q.append((i, j, k))
            elif line[j] == -1:
                total -= 1
        box.append(line)
    boxes.append(box)

if complete == total:
    print(0)
else:
    while complete < total:
        if not q:
            day = -1
            break
        nq = []
        for y, x, z in q:
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < n and 0 <= nx < m and boxes[z][ny][nx] == 0:
                    boxes[z][ny][nx] = 1
                    complete += 1
                    nq.append((ny, nx, z))

            for dz in [1, -1]:
                nz = z + dz
                if 0 <= nz < h and boxes[nz][y][x] == 0:
                    boxes[nz][y][x] = 1
                    complete += 1
                    nq.append((y, x, nz))
        day += 1
        q = nq

    print(day)