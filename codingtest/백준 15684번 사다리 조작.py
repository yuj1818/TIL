import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def game():
    res = 0
    for i in range(n):
        x = i
        for y in range(h):
            if ladder[y][x] != -1: x = ladder[y][x]
        if x == i: res += 1
    return res

def dfs(cnt, d):
    global ans
    if ans != -1: return
    connected = game()
    if connected + (d - cnt) * 2 < n: return
    if cnt == d:
        if connected == n: ans = cnt
        return
    for i in range(h):
        for j in range(n - 1):
            if ladder[i][j] == -1 and ladder[i][j + 1] == -1:
                ladder[i][j], ladder[i][j + 1] = j + 1, j
                dfs(cnt + 1, d)
                ladder[i][j], ladder[i][j + 1] = -1, -1

n, m, h = map(int, input().split())
ladder = [[-1] * n for _ in range(h)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    ladder[a][b] = b + 1
    ladder[a][b + 1] = b
ans = -1
for d in range(4):
    dfs(0, d)
    if ans != -1: break
print(ans)