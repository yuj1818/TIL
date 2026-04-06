import sys
input = sys.stdin.readline
n = int(input())
ans = 2
for x in input().rstrip():
    if x == 'S': ans += 2
    else: ans += 1
if ans == (n + 1) * 2: ans -= 2
print(ans // 2)
