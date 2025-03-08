import sys
input = sys.stdin.readline
a=[int(input()) for _ in range(int(input()))]
print('\n'.join(map(str, sorted(a))))