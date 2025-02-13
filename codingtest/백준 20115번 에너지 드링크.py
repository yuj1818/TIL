import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
mv = max(a)
print((sum(a) - mv) / 2 + mv)