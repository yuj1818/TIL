import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        cnt = board[i][j]
        if not cnt or not dp[i][j]: continue
        if i + cnt < n: dp[i + cnt][j] += dp[i][j]
        if j + cnt < n: dp[i][j + cnt] += dp[i][j]
print(dp[-1][-1])