MIN = -float('inf')
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [[MIN] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0
ans = MIN

for i in range(1, n + 1):
    is_minus = arr[i] < 0
    for j in range(k + 1):
        if is_minus:
            if j > 0:
                dp[i][j] = max(arr[i], dp[i - 1][j - 1] + arr[i])
        else:
            dp[i][j] = max(arr[i], dp[i - 1][j] + arr[i])
        ans = max(dp[i][j], ans)

print(ans)