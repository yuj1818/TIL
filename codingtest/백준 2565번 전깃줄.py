import sys

input = sys.stdin.readline
n = int(input())
L = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if L[j][1] < L[i][1]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
print(n - max(dp))
