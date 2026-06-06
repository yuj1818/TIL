N, M, y, x = map(int, input().split())
d = {'L': [(0, -1), [(0, 5), (1, 4), (2, 2), (3, 3), (4, 0), (5, 1)]], 
    'R': [(0, 1), [(0, 4), (1, 5), (2, 2), (3, 3), (4, 1), (5, 0)]], 
    'U': [(-1, 0), [(0, 3), (1, 2), (2, 0), (3, 1), (4, 4), (5, 5)]], 
    'D': [(1, 0), [(0, 2), (1, 3), (2, 1), (3, 0), (4, 4), (5, 5)]]}
nums = [1, 6, 2, 5, 3, 4]
grid = [[0] * N for _ in range(N)]
y, x = y - 1, x - 1
grid[y][x] = 6
for o in input().split():
    ny, nx = y + d[o][0][0], x + d[o][0][1]
    if not (0 <= ny < N and 0 <= nx < N): continue
    tmp = nums[:]
    for s, e in d[o][1]: tmp[e] = nums[s]
    nums = tmp
    y, x = ny, nx
    grid[y][x] = nums[1]
ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]: ans += grid[i][j]
print(ans)