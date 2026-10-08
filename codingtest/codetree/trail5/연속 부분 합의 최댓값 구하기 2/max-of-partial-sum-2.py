n = int(input())
a = list(map(int, input().split()))
cur = 0
ans = -1 * float('inf')
for x in a:
    cur += x
    ans = max(ans, cur)
    if cur < 0: cur = 0
print(ans)