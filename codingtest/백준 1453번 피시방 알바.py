import sys
n = int(sys.stdin.readline())
ans = 0
s = set()
for x in list(map(int, sys.stdin.readline().split())):
    if x in s: ans += 1
    else: s.add(x)
print(ans)