import sys
input = sys.stdin.readline
n = int(input())
p = dict()
for x in input().strip().split(): p[x] = 0
for _ in range(n):
    for x in input().strip().split(): p[x] += 1
for name, v in sorted(p.items(), key=lambda x: (-x[1], x[0])): print(name, v)