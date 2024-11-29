def calc(v, acc, nxt, f):
    if v == n:
        if acc + nxt == 0:
            print(f)
        return
    nv = v + 1
    calc(nv, acc, nxt * 10 + (nv if nxt > 0 else -nv), f + ' ' + str(nv))
    calc(nv, acc + nxt, nv, f + '+' + str(nv))
    calc(nv, acc + nxt, -nv, f + '-' + str(nv))

for _ in range(int(input())):
    n = int(input())
    f = []
    calc(1, 0, 1, '1')
    print()