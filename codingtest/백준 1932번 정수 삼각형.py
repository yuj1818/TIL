import sys

n = int(input())
triangle = []
dp = [[0] * i for i in range(1, n + 1)]

for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

dp[-1] = triangle[-1]

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        dp[i][j] = max(triangle[i][j] + dp[i + 1][j], triangle[i][j] + dp[i + 1][j + 1])

print(dp[0][0])