n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
ans = 1
s, e = meetings[0]
for i in range(1, n):
    ns, ne = meetings[i]
    if ns < e: continue
    ans += 1
    s, e = ns, ne
print(n - ans)