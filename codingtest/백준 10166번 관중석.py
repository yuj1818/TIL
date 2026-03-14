import sys, math
s, e = map(int, sys.stdin.readline().split())
ans = 0
for i in range(s, e + 1):
    for j in range(i):
        v = i // math.gcd(i, j)
        if ((s + v - 1) // v) * v >= i: ans += 1
print(ans)