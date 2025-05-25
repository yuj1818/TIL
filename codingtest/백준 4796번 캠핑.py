import sys
input = sys.stdin.readline
t = 1
while 1:
    l, p, v = map(int, input().split())
    if l + p + v == 0: break
    a, b = divmod(v, p)
    sys.stdout.write(f'Case {t}: {(a + 1) * l if b > l else b + a * l}\n')
    t += 1