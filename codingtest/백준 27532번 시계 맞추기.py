import sys
input = sys.stdin.readline
M = int(input())
a = []
for _ in range(M):
    h, m = map(int, input().split(':'))
    a.append(h % 12 * 60 + m)
ans = float('inf')
for r in range(720):
    s = set()
    for x in range(M):
        v = (a[x] - r * x) % 720
        s.add(v)
    ans = min(ans, len(s))
print(ans)
