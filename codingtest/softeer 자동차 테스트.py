import sys
input = sys.stdin.readline
n, q = map(int, input().split())
cars = list(map(int, input().split()))
cars.sort()
d = dict()
for i in range(n):
    d[cars[i]] = i * (n - i - 1)
for _ in range(q):
    m = int(input())
    try:
        print(d[m])
    except:
        print(0)