n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append([y, x])
a.sort()
i, j = 0, n - 1
ans = 0
while i < j:
    cnt = min(a[i][1], a[j][1])
    ans = max(a[i][0] + a[j][0], ans)
    a[i][1] -= cnt
    if a[i][1] == 0: i += 1
    a[j][1] -= cnt
    if a[j][1] == 0: j -= 1
if i == j: ans = max(a[i][0] * 2, ans)
print(ans)