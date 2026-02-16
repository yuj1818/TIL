import sys
input = sys.stdin.readline
while 1:
    g, t, a, d = map(int, input().split())
    if g < 0: break
    x, y = 0, 0
    gcnt = t * (t - 1) // 2 * g
    tcnt = g * a + d
    tmp = 1
    while tcnt > tmp:
        x += tmp
        tmp *= 2
    y += tmp - tcnt
    x += gcnt
    print(f"{g}*{a}/{t}+{d}={x}+{y}")