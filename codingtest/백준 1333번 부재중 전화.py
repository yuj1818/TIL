n, l, d = map(int, input().split())
l += 5
x, t = 0, d
for i in range(n):
    x += l
    while 1:
        if t < x - 5: t += d
        else: break
    if x - 5 <= t < x: break
print(t)