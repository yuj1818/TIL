MIN = -float('inf')
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3] + [[MIN] * 3 for _ in range(n)]
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if j == k: continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + arr[i - 1][j])
print(max(dp[-1]))