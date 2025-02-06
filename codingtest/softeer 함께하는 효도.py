from copy import deepcopy
from itertools import permutations
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
pos = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(n)]
for y, x in pos:
    visited[y][x] = 1
    
def dfs(y, x, cnt, t, path):
    global q, mvisited, mpath
    if cnt == 3:
        if q < t: 
            q = t
            mvisited = deepcopy(nvisited)
            mpath = path[:]
        return
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in total_path[cnt]:
            if not nvisited[ny][nx]:
                nvisited[ny][nx] = 1
                dfs(ny, nx, cnt + 1, t + trees[ny][nx], path + [(ny, nx)])
                nvisited[ny][nx] = 0
            else:
                dfs(ny, nx, cnt + 1, t, path + [(ny, nx)])
ans = 0
for seq in permutations(pos, m):
    total_path = {0: set(pos), 1: set(), 2: set(), 3: set()}
    nvisited = deepcopy(visited)
    mvisited = deepcopy(visited)
    total = 0
    for y, x in seq:
        q = 0
        mpath = []
        dfs(y, x, 0, trees[y][x], [(y, x)])
        nvisited = deepcopy(mvisited)
        total += q
        for i in range(1, 4):
            total_path[i].add(mpath[i - 1])
    if ans < total: ans = total
print(ans)