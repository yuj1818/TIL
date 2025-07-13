import sys
input = lambda:sys.stdin.readline().strip()
s = input()
ans = 0
for _ in range(int(input())):
    x = input()
    if s in x + x: ans += 1
print(ans)