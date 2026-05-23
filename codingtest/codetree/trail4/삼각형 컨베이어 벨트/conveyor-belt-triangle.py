from collections import deque
n, t = map(int, input().split())
l = deque(map(int, input().split()))
r = deque(map(int, input().split()))
d = deque(map(int, input().split()))
for _ in range(t):
    ln, rn, dn = l.pop(), r.pop(), d.pop()
    l.appendleft(dn)
    r.appendleft(ln)
    d.appendleft(rn)
for x in [l, r, d]:
    print(*x)