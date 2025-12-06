n = int(input())
s, e, t, ans = 1, 1, 1, 1
if n == 1 or n == 2:
    print(1)
    exit()
while e < n // 2 + 2:
    if t == n:
        ans += 1
        e += 1
        t += e
    elif t < n:
        e += 1
        t += e
    else:
        t -= s
        s += 1
print(ans)