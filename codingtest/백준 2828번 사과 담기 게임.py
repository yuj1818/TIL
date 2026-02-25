import sys

input = sys.stdin.readline
n, m = map(int, input().split())
l, r = 0, m
ans = 0
for _ in range(int(input())):
    i = int(input())
    if i < l:
        ans += l - i
        l, r = i, i + m - 1
    elif i > r:
        ans += i - r
        l, r = i - m + 1, i
print(ans)
