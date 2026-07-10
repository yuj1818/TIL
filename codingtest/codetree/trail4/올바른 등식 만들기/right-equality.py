n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
total = sum(arr)
LIM = min(total * 2, 40)
dp = [[0] * (LIM + 1) for _ in range(n + 1)]
dp[0][LIM // 2] = 1
m += LIM // 2
for i in range(1, n + 1):
    for j in range(LIM + 1):
        if j >= arr[i]:
            dp[i][j] += dp[i - 1][j - arr[i]]
        if j + arr[i] <= LIM:
            dp[i][j] += dp[i - 1][j + arr[i]]
print(dp[n][m])