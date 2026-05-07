def backtrack(idx, cw, cv):
    global mv
    if idx == m:
        if cw <= c:
            mv = max(mv, cv)
        return
    backtrack(idx + 1, cw, cv)
    backtrack(idx + 1, cw + tmp[idx], cv + tmp[idx] ** 2)

def get_v(i, j):
    global tmp, mv
    tmp = graph[i][j:j + m]
    mv = 0
    backtrack(0, 0, 0)
    return mv

n, m, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
v_map = [[0] * n for _ in range(n)]
tmp = []
mv = 0
for i in range(n):
    for j in range(n - m + 1):
        v_map[i][j] = get_v(i, j)
ans = 0
for y1 in range(n):
    for x1 in range(n - m + 1):
        for y2 in range(n):
            if y1 == y2 and n - m < m: continue
            for x2 in range((0 if y1 != y2 else x1 + m), n - m + 1):
                ans = max(ans, v_map[y1][x1] + v_map[y2][x2])
print(ans)
