import sys
input = sys.stdin.readline
MAX = 2 ** 31
N = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]
nums = [*map(int, input().split())]
for i in range(1,  N):
    _, b = map(int, input().split())
    nums.append(b)

for j in range(1, N+1):
    for i in range(j-1, 0, -1):
        mv = MAX
        for k in range(i, j):
            v = dp[i][k]+dp[k+1][j]+nums[i-1]*nums[k]*nums[j]
            if mv > v: mv = v
        dp[i][j] = mv

print(dp[1][-1])