k = int(input())
n = 1
while n < k: n *= 2
if k == n:
    print(n, 0)
    exit()
cnt, l, s = 0, k, n
while l > 0:
    if l >= s: l -= s
    else:
        s //= 2
        cnt += 1
print(n, cnt)
