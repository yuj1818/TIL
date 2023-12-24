import sys

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre_sum = [0] * (n + 1)
for i in range(0, n):
    pre_sum[i + 1] = pre_sum[i] + nums[i]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(pre_sum[e] - pre_sum[s - 1])