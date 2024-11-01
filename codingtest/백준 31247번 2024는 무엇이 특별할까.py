import sys
tc = int(sys.stdin.readline())
for _ in range(tc):
    n, k = map(int, sys.stdin.readline().split())
    if k > 60:
        print(0)
    else:
        print(((n // (2 ** k) + 1) // 2))