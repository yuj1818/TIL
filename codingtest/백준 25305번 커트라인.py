import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = sorted(map(int, input().split()), reverse=True)
print(s[:k][-1])
