n, m = map(int, input().split())
arr =[tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    for w, v in arr:
        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)
print(max(dp))