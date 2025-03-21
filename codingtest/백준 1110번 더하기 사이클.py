import sys
ans = 0
n = int(sys.stdin.readline())
tmp = n
while 1:
    x, y = tmp // 10, tmp % 10
    tmp = y * 10 + (x + y) % 10
    ans += 1
    if n == tmp: break
print(ans)