import sys

input = sys.stdin.readline
n, m = map(int, input().split())
if n == 0:
    print(0)
    sys.exit()
w, ans = 0, 0
for x in list(map(int, input().split())):
    w += x
    if w > m:
        ans += 1
        w = x
if w > 0:
    ans += 1
print(ans)
