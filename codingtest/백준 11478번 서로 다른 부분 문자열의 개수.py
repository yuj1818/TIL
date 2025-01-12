import sys
s = sys.stdin.readline().strip()
n = len(s)
ans = set()
for i in range(n):
    x = ''
    for j in range(i, n):
        x += s[j]
        ans.add(x)
print(len(ans))