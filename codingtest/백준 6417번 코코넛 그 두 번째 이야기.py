import sys

for n in list(map(int, sys.stdin.readlines())):
    if n == -1:
        break
    sig = 0
    for k in range(n, 1, -1):
        c = n
        for _ in range(k):
            if (c - 1) % k:
                break
            c -= c // k + 1
        else:
            if c % k:
                print(f"{n} coconuts, no solution")
            else:
                print(f"{n} coconuts, {k} people and 1 monkey")
                sig = 1
            break
    if not sig:
        print(f"{n} coconuts, no solution")
