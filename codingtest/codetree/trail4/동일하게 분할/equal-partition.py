n = int(input())
arr = list(map(int, input().split()))
t = sum(arr)
if t % 2:
    print('No')
    exit()
MAX = t // 2
dp = [0] * (MAX + 1)
dp[0] = 1
for x in arr:
    for i in range(MAX, x - 1, -1):
        if dp[i - x]: dp[i] = 1
if dp[-1]: print('Yes')
else: print('No')
