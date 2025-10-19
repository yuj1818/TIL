import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    t = sum(map(int, input().split()))
    d = 1
    while t <= n:
        t *= 4
        d += 1
    print(d)