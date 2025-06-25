x, y, w, s = map(int, input().split())
if x == y: print(min(s * x, (x + y) * w))
else:
    rest = abs(x - y)
    print(min(s * min(x, y) + min(w * rest, (s * rest if rest % 2 == 0 else s * (rest - 1) + w)), w * (x + y)))