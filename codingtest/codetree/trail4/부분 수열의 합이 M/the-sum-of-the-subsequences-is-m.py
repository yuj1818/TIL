MAX = float('inf')
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [MAX] * (m + 1)
dp[0] = 0
for i in range(n):
    for j in range(m, -1, -1):
        if arr[i] <= j:
            if dp[j - arr[i]] == MAX: continue
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)
if dp[-1] == MAX:
    print(-1)
else:
    print(dp[-1])