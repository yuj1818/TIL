import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
pre = input()
ans = 0
for _ in range(n - 1):
    x = input()
    if pre > x: ans -= 1
    else: ans += 1
    pre = x
if ans == n - 1: print('INCREASING')
elif ans == -n + 1: print('DECREASING')
else: print('NEITHER')