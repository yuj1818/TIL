import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mp, ms = int(1e9), int(1e9)
for _ in range(m):
    p, s = map(int, input().split())
    mp = min(mp, p)
    ms = min(ms, s)
if mp > ms * 6:
    print(ms * n)
elif mp < ms * (n % 6):
    print(mp * (n // 6 + 1))
else:
    print((n // 6) * mp + (n % 6) * ms)
