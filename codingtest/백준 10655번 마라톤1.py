import sys
input = sys.stdin.readline
n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
md, total = 0, 0
total += abs(x2 - x1) + abs(y2 - y1)
for i in range(n - 2):
    x3, y3 = map(int, input().split())
    d12 = abs(x2 - x1) + abs(y2 - y1)
    d23 = abs(x3 - x2) + abs(y3 - y2)
    d13 = abs(x3 - x1) + abs(y3 - y1)
    if md < d12 + d23 - d13: md = d12 + d23 - d13
    total += d23
    x1, y1 = x2, y2
    x2, y2 = x3, y3
print(total - md)