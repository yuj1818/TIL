import sys
cnt = {'c': 26, 'd': 10}
s = sys.stdin.readline().rstrip()
ans = 0
for i, x in enumerate(s):
    if i == 0:
        ans += cnt[x]
        continue
    v = cnt[x]
    if x == s[i - 1]: v -= 1
    ans *= v
print(ans)