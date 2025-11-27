import sys
input = sys.stdin.readline
s, e = int(input()), int(input())
ans = [0, 0]
for i in range(s, e + 1):
    if i < 2: continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0: break
    else:
        if ans[0] == 0: ans[-1] = i
        ans[0] += i
if ans[0] == 0: print(-1)
else:
    print(ans[0])
    print(ans[1])