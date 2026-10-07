n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0
res = k
while coins and res > 0:
    x = coins.pop()
    d, m = divmod(res, x)
    ans += d
    res = m
print(ans)