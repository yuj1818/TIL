import sys
input = sys.stdin.readline

def daq(a, b, c):
    if b == 1:
        return a % c

    n = daq(a, b // 2, c)
    if b % 2 == 0:
        return (n * n) % c
    else:
        return (n * n * a) % c

print(daq(*map(int, input().split())))