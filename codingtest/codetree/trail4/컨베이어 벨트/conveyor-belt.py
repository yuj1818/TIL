from collections import deque
n, t = map(int, input().split())
u = deque(map(int, input().split()))
d = deque(map(int, input().split()))
for _ in range(t):
    un, dn = u.pop(), d.pop()
    u.appendleft(dn)
    d.appendleft(un)
print(*u)
print(*d)