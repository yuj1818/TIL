import sys
input = sys.stdin.readline
ans = 0
n = int(input())
h = list(map(int, input().split())) + [0]
s = h[0]
for i in range(1, n + 1):
    if h[i] <= h[i - 1]:
        ans = max(h[i - 1] - s, ans)
        s = h[i]
print(ans)