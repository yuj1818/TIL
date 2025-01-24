import sys
input = sys.stdin.readline
n, w, l = map(int, input().split())
a = list(map(int, input().split()))
s, e, sec, cw = 0, 0, 0, 0
ans = [-1] * n
while s < n:
    if ans[e] == sec:
        cw -= a[e]
        e += 1
    if cw + a[s] <= l:
        ans[s] = sec + w
        cw += a[s]
        s += 1
    else:
        sec = ans[e] - 1
    sec += 1
print(ans[-1] + 1)