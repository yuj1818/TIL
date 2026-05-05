n, m = map(int, input().split())
d = dict()
for i in range(1, n + 1):
    w = input()
    d[str(i)] = w
    d[w] = i
for _ in range(m):
    print(d[input()])
