n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
MAX = total // 2
dp = [0] * (MAX + 1)
dp[0] = 1
for x in arr:
    for i in range(MAX, x - 1, -1):
        dp[i] |= dp[i - x]
ans = total
for i in range(MAX, -1, -1):
    if dp[i]:
        ans = min(ans, total - 2 * i)
print(ans)