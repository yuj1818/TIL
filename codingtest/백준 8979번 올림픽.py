import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countries = [tuple(map(int, input().split())) for _ in range(n)]
countries.sort(key= lambda x: (-x[1], -x[2], -x[3]))
rank, e = 0, 1
pre = (-1, -1, -1)
for c, g, s, b in countries:
    if pre != (g, s, b):
        rank += e
        e = 1
    else:
        e += 1
    if c == k:
        print(rank)
        break
    pre = (g, s, b)