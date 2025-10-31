n = int(input())
dp = [0, 0]
for i in range(2, n + 1):
    x = i // 2
    if i % 2:
        dp.append(x * (x + 1) + dp[x] + dp[x + 1])
    else:
        dp.append(x ** 2 + dp[x] * 2)
print(dp[-1])