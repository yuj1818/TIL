import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    a[i - 1:j] = a[i - 1:j][::-1]
print(' '.join(map(str, a)))