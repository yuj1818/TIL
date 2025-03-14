import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
home = []
store = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1: home.append((i, j))
        elif grid[i][j] == 2: store.append((i, j))

def find(tdist, sn, hn):
    ans = float('inf')
    dist = [float('inf')] * hn

    def compare(dist, i):
        return [a if a < b else b for a, b in zip(dist, tdist[i])]

    def dfs(dist, si, d):
        nonlocal ans
        if d == m:
            res = sum(dist)
            if ans > res: ans = res
            return
        for i in range(si, sn):
            dfs(compare(dist, i), i + 1, d + 1)

    dfs(dist, 0, 0)
    return ans

tdist = [[abs(hy - sy) + abs(hx - sx) for hy, hx in home] for sy, sx, in store]
print(find(tdist, len(store), len(home)))