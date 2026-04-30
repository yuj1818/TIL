from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
points = sorted(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]
for a, b in queries:
    na = bisect_left(points, a)
    nb = bisect_right(points, b)
    print(nb - na)
