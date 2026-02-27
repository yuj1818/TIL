import sys

input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
    sys.exit()
d = int(input())
c = [int(input()) for _ in range(n - 1)]
ans = 0
while d <= max(c):
    d += 1
    ans += 1
    c[c.index(max(c))] -= 1
print(ans)
