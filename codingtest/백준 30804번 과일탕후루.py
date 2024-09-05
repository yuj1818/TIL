from collections import defaultdict

n = int(input())
tang = input().split()
fruits = defaultdict(int)
l, cnt, ans = 0, 0, 0

for r in range(n):
    if fruits[tang[r]] == 0:
        cnt += 1
    fruits[tang[r]] += 1

    while cnt > 2:
        fruits[tang[l]] -= 1
        if fruits[tang[l]] == 0:
            cnt -= 1
        l += 1

    ans = max(ans, r-l+1)

print(ans)