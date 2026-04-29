n, q = map(int, input().split())
points = sorted(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]
a = [0] * 1000001
for i in range(1, n):
    for x in range(points[i - 1], points[i]):
        a[x] = i
else:
    for x in range(points[-1], 1000001): a[x] = n
for s, e in ranges:
    print(a[e] - (a[s - 1] if s > 0 else 0))
