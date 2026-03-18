import sys

sys.setrecursionlimit(10**6)


def F(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if not f[x]:
        v = F(x - 1) + F(x - 2)
        f[x] = v
        return v
    return f[x]


f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597] + [
    0
] * 9983
print(F(int(input())))
