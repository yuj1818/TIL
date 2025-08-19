import sys
input = sys.stdin.readline
n = int(input())
guitars = [input().strip() for _ in range(n)]
guitars.sort(key=lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))
print('\n'.join(guitars))