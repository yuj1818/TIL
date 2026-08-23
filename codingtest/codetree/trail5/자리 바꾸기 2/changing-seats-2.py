n, k = map(int, input().split())
d = {i: set([i]) for i in range(1, n + 1)}
arr = [tuple(map(int, input().split())) for _ in range(k)]
pos = list(range(n + 1))
for _ in range(3):
    for a, b in arr:
        na, nb = pos[a], pos[b]
        d[na].add(b)
        d[nb].add(a)
        pos[a], pos[b] = pos[b], pos[a]
for i in range(1, n + 1):
    print(len(d[i]))