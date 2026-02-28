import sys
n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
ans = 0
for i in range(n - 2, -1, -1):
    if s[i] < s[i + 1]: continue
    v = s[i] - s[i + 1] + 1
    s[i] -= v
    ans += v
print(ans)