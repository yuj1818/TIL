n = int(input())
price = list(map(int, input().split()))
min_v, ans = price[0], 0
for i in range(1, n):
    p = price[i] - min_v
    if ans < p: ans = p
    if price[i] < min_v: min_v = price[i]
print(ans)