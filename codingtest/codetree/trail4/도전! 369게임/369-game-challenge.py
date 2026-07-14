MOD = 10 ** 9 + 7
n = input()
l = len(n)
a = [1] * (l + 1)
for i in range(1, l + 1):
    a[i] = a[i - 1] * 10 % MOD
dp = [[0] * 3 for _ in range(100001)]
ans = 0
sig = 0
t = 0
for i in range(l):
    num = int(n[i])
    for x in range(10):
        if x != 0 and not x % 3:
            ans += (dp[i][0] + dp[i][1] + dp[i][2]) * a[l - i - 1] % MOD
            ans %= MOD
            continue
        for k in range(3):
            dp[i + 1][(x + k) % 3] += dp[i][k]
            dp[i + 1][(x + k) % 3] %= MOD
    for x in range(num):
        if sig or (x != 0 and not x % 3):
            ans += a[l - i - 1]
            ans %= MOD
        else:
            dp[i + 1][(x + t) % 3] += 1
            dp[i + 1][(x + t) % 3] %= MOD
    
    if num != 0 and not num % 3:
        sig = 1
    else:
        t += num
    
if sig:
    ans += 1
    ans %= MOD
else:
    dp[l][t % 3] += 1
    dp[l][t % 3] %= MOD

ans += dp[l][0]
ans += (MOD - 1)
ans %= MOD
print(ans)
