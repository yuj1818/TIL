import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
f = [0] * n
f[0], ans = arr[0], arr[0]
for i in range(1, n):
    f[i] = max(f[i - 1] + arr[i], arr[i])
    if ans < f[i]: ans = f[i]
print(ans)