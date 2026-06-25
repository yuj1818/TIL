n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
dp = [1] * n
for i in range(1, n):
    x1, x2 = lines[i]
    for j in range(i):
        px1, px2 = lines[j]
        if px2 < x1: dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))