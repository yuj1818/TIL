import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
ans = [0] * n
for i in range(n - 1):
    a = 0
    for j in range(i + 1, n):
        na = (heights[j] - heights[i]) / (j - i)
        if j == i + 1 or a < na:
            a = na
            ans[i] += 1
        else: continue
for i in range(n - 1, 0, -1):
    a = 0
    for j in range(i - 1, -1, -1):
        na = (heights[j] - heights[i]) / (i - j)
        if j == i - 1 or a < na:
            a = na
            ans[i] += 1
        else: continue
print(max(ans))