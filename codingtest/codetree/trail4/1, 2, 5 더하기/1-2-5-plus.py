n = int(input())
nums = [1, 2, 5]
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for x in nums:
        if i >= x: dp[i] = (dp[i] + dp[i - x]) % 10007
print(dp[-1])