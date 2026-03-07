import sys
k, a, b = map(int, sys.stdin.readline().split())
if a < 0 and b < 0: a, b = -b, -a
ans = 0 if a > 0 else 1
ans += b // k + (-((a - 1) // k) if a > 0 else -a // k)
print(ans)