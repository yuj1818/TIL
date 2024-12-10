import sys

def main():
    n, h = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        h -= a[i]
        if h <= 0: return i + 1
    else: return -1

print(main())