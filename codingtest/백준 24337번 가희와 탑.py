import sys
n, l, r = map(int, sys.stdin.readline().split())
if l <= r:
    if l == 1: ans = [r] + [1] * (n - r) + list(range(r - 1, 0, -1))
    else: ans = [1] * (n - r - l + 1) + list(range(1, l)) + list(range(r, 0, -1))
else: ans = [1] * (n - l - r + 1) + list(range(1, l + 1)) + list(range(r - 1, 0, -1))
print(' '.join(map(str, ans)) if len(ans) == n else -1)