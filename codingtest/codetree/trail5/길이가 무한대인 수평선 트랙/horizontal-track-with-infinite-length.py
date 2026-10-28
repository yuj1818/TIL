from sortedcontainers import SortedSet
n, t = map(int, input().split())
players = [list(map(int, input().split())) for _ in range(n)]
ep = SortedSet()
for s, v in players:
    e = s + v * t
    p = ep.bisect_left(e)
    while p != len(ep):
        ep.remove(ep[p])
        p = ep.bisect_left(e)
    ep.add(e)
print(len(ep))