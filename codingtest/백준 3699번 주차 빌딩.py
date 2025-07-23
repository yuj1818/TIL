import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h, l = map(int, input().split())
    cars = dict()
    for i in range(h):
        row = list(map(int, input().split()))
        for j in range(l):
            if row[j] != -1:
                cars[row[j]] = (i + 1, j + 1)
    cars = sorted(cars.items())
    pos = [1] * (h + 1)
    ans = 0
    for i, (y, x) in cars:
        ans += abs(y - 1) * 20
        ans += min(abs(pos[y] - x), abs(l - abs(pos[y] - x))) * 5
        pos[y] = x
    print(ans)