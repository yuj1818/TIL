import math
from functools import reduce


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solution(signals):
    P = reduce(lcm, [sum(s) for s in signals])
    for t in range(1, P + 1):
        sig = 1
        for g, y, r in signals:
            p = g + y + r
            m = t % p
            if not g <= m <= g + y - 1:
                sig = 0
                break
        if sig:
            return t + 1
    return -1
