import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

tc = int(input())
dp = [0, 1, 1, 1, 2, 2] + [0] * 95

for i in range(6, 101):
    dp[i] = dp[i - 5] + dp[i - 1]

for _ in range(tc):
    n = int(input())
    print(dp[n])