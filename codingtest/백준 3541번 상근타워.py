import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ans = int(1e9)
for _ in range(m):
    u, d = map(int, input().split())
    l, r = 0, n
    while l <= r:
        mid = (l + r) // 2
        f = u * mid - d * (n - mid)
        if f > 0:
            ans = min(ans, f)
            r = mid - 1
        else: l = mid + 1
print(ans)