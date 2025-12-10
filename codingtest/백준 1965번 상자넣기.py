from bisect import bisect_left
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
s = [a[0]]
for i in range(1, n):
    if a[i] > s[-1]: s.append(a[i])
    else:
        s[bisect_left(s, a[i])] = a[i]
print(len(s))