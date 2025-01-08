import sys
n, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
c, ans = 0, 0
for i in range(n):
    c += a[i]
    if i >= l: c -= a[i - l]
    if 129 <= c <= 138: ans += 1
sys.stdout.write(str(ans))