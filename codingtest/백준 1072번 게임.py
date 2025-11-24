x, y = map(int, input().split())
z = (100 * y) // x
l, r, ans = 0, x, x
if z >= 99: print(-1)
else:
    while l <= r:
        mid = (l + r) // 2
        if (100 * (y + mid)) // (x + mid) > z:
            ans, r = mid, mid - 1
        else: l = mid + 1
    print(ans)