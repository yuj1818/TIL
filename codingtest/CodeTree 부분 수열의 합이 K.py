n, k = map(int, input().split())
arr = list(map(int, input().split()))
s, e, v = 0, 0, arr[0]
cnt = 0
while 1:
    if v < k:
        e += 1
        if e >= n: break
        v += arr[e]
    else:
        if v == k: cnt += 1
        v -= arr[s]
        s += 1
print(cnt)
