import sys
i, ans = 0, 1
for x in sys.stdin.readline().rstrip():
    ci = ord(x)
    if ci <= i: ans += 1
    i = ci
print(ans)