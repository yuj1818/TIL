import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
if n == 1 and a[0] == 1:
    print('Happy')
else:
    print('Happy' if (max(a) <= sum(a) // 2) else 'Unhappy')
