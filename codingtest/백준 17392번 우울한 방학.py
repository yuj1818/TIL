import sys
n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split())) if n else []
t = m - sum(h) - n
if t <= 0:
    print(0)
    sys.exit()
s, r = divmod(t, n + 1)
v = sum([x ** 2 for x in range(1, s + 1)])
ans = v * (n + 1 - r) + (v + (s + 1) ** 2) * r
print(ans)