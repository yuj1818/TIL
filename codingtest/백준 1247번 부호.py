import sys
input = sys.stdin.readline
for _ in range(3):
    n = int(input())
    res = sum([int(input()) for _ in range(n)])
    if res == 0: print('0')
    else: print('+' if res > 0 else '-')