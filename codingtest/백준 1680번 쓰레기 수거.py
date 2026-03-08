import sys
input = sys.stdin.readline
for _ in range(int(input())):
    W, N = map(int, input().split())
    cw, cx, d = 0, 0, 0
    for _ in range(N):
        x, w = map(int, input().split())
        d += x - cx
        if cw + w > W:
            d += x * 2
            cw, cx = w, x
        elif cw + w == W:
            d += x
            cw, cx = 0, 0
        else:
            cw += w
            cx = x
    print(d + cx)