import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    n = int((-1 + (1 + 4 * d) ** (1 / 2)) / 2)
    r = d - n * (n + 1)
    if 0 < r <= n + 1: print(2 * n + 1)
    elif r > n + 1: print(2 * n + 2)
    else: print(2 * n)