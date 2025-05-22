import sys
input = lambda: sys.stdin.readline().strip()
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    ans = 0
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    dv = [[] for _ in range(26)]
    kv = [0] * 26
    for k in keys: kv[k - 97] = 1
    q = [(0, 0)]
    visited[0][0] = 1
    while q:
        tmp = []
        for y, x in q:
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if not(0 <= ny < h + 2 and 0 <= nx < w + 2) or visited[ny][nx] or building[ny][nx] == 42: continue
                v = building[ny][nx]
                if v == 36: ans += 1
                elif 65 <= v <= 90:
                    if not kv[v - 65]:
                        dv[v - 65].append((ny, nx))
                        continue
                elif 97 <= v <= 122:
                    kv[v - 97] = 1
                    if dv[v - 97]: tmp.extend(dv[v - 97])
                tmp.append((ny, nx))
                visited[ny][nx] = 1
        q = tmp
    return ans

for _ in range(int(input())):
    h, w = map(int, input().split())
    building = [[46] * (w + 2)] + [[46] + list(map(ord, input())) + [46] for _ in range(h)] + [[46] * (w + 2)]
    keys = input()
    keys = list(map(ord, keys)) if keys != '0' else []
    print(bfs())