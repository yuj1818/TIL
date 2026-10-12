n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: x[1])
ans = 0
cs, ce = 0, 0
for s, e in meetings:
    if s >= ce:
        ans += 1
        cs, ce = s, e
print(ans)