import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set([input().strip() for _ in range(n)])
ans = 0
for _ in range(m):
    if input().strip() in s: ans += 1
print(ans)