MAX = float('inf')
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = MAX
dp = [[MAX] * n for _ in range(n)]

def init_dp():
    dp[0][0] = grid[0][0]
    for x in range(1, n):
        dp[x][0] = max(dp[x - 1][0], grid[x][0])
        dp[0][x] = max(dp[0][x - 1], grid[0][x])

def find_max_v(min_v):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < min_v: grid[i][j] = MAX
    init_dp()
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(grid[i][j], min(dp[i - 1][j], dp[i][j - 1]))
    return dp[-1][-1]

for min_v in range(1, 101):
    max_v = find_max_v(min_v)
    if max_v == MAX: continue
    ans = min(ans, max_v - min_v)
print(ans)