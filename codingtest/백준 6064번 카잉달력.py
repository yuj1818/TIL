import sys
input = sys.stdin.readline

def gcd(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

def calc(m, n, x, y, lcm):
    k = x
    while k <= lcm:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1

tc = int(input())
for _ in range(tc):
    m, n, x, y = map(int, input().split())
    lcm = m * n // gcd(m, n)

    if m < n:
        m, n = n, m
        x, y = y, x

    print(calc(m, n, x, y, lcm))