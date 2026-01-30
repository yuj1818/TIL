import sys
input = sys.stdin.readline
w, h = map(int, input().split())
z = max(w, h)
maps = []
pos = []
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(h):
    line = list(input())
    maps.append(line)
    for j in range(w):
        if line[j] == 'C': pos.append((i, j))
s = [pos[0]]
visited = [[-1] * w for _ in range(h)]
visited[pos[0][0]][pos[0][1]] = 0
cnt = 0
while s:
    ns = []
    while s:
        y, x = s.pop()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            for _ in range(z - 1):
                if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] != '*':
                    if visited[ny][nx] == -1:
                        visited[ny][nx] = cnt
                        ns.append((ny, nx))
                        if ny == pos[1][0] and nx == pos[1][1]:
                            print(cnt)
                            sys.exit()
                    elif visited[ny][nx] < cnt: break
                else: break
                ny += dy
                nx += dx
    s = ns
    cnt += 1