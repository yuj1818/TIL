import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
s, e = 0, n - 1
df = abs(a[0] + a[-1])
ans = [a[0], a[-1]]
while s < e:
    l, r = a[s], a[e]
    v = l + r
    if abs(v) < df:
        df = abs(v)
        ans = [l, r]
        if df == 0: break
    if v < 0: s += 1
    else: e -= 1
print(' '.join(map(str, ans)))