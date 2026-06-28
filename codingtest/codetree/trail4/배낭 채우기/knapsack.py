n, m = map(int, input().split())
arr =[tuple(map(int, input().split())) for _ in range(n)]
dp = [-1] * (m + 1)
dp[0] = 0
for w, v in arr:
    for i in range(m, -1, -1):
        if i >= w:
            if dp[i - w] == -1: continue
            dp[i] = max(dp[i], dp[i - w] + v)
print(max(dp))