import sys
input = sys.stdin.readline
n, l = map(int, input().split())
h = sorted(map(int, input().split()))
for x in h:
    if l >= x: l += 1
print(l)