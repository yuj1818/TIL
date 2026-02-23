ans = ''
for x in input().split('.'):
    if x:
        l = len(x)
        if l % 2:
            print(-1)
            exit()
        if l >= 4:
            ans += 'AAAA' * (l // 4)
            l %= 4
        if l >= 2:
            ans += 'BB' * (l // 2)
            l %= 2
        if l > 0:
            print(-1)
            exit()
    ans += '.'
print(ans[:-1])
