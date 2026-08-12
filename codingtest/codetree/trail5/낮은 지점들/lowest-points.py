n = int(input())
points = dict()
for _ in range(n):
    x, y = map(int, input().split())
    if x in points:
        cy = points[x]
        if cy > y: points[x] = y
    else: points[x] = y
print(sum(points.values()))