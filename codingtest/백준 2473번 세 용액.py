n = int(input())
liq = list(map(int, input().split()))
liq.sort()
mv = 3000000001
ans = tuple()
for i in range(n - 2):
    f = liq[i]
    s, t = i + 1, n - 1
    while s < t:
        mix = f + liq[s] + liq[t]
        if abs(mix) < mv:
            mv = abs(mix)
            ans = (f, liq[s], liq[t])
        if mix > 0: t -= 1
        elif mix < 0: s += 1
        else:
            print(' '.join(map(str, ans)))
            exit()
print(' '.join(map(str, ans)))