n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
dp = [jobs[i][-1] for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            dp[i] = max(dp[i], dp[j] + jobs[i][-1])
print(max(dp))