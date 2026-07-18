MIN = -float('inf')
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[MIN] * 3 for _ in range(3)] for _ in range(n+1)]
for j in range(3):
    dp[1][j][j] = arr[0][j]
for i in range(2, n + 1):
    for j in range(3):
        for k in range(3): 
            for l in range(3):
                if k == l: continue
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l] + arr[i - 1][k])

ans = 0
for j in range(3):
    for k in range(3):
        if j == k: continue
        ans = max(ans, dp[-1][j][k])
print(ans)