import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]

def bs(s, e, t):
    while s < e:
        mid = (s + e) // 2
        if t > seq[mid]: s = mid + 1
        else: e = mid
    return e

seq = [a[0]]
for i in range(1, n):
    if a[i] > seq[-1]:
        seq.append(a[i])
    else:
        ni = bs(0, len(seq) - 1, a[i])
        seq[ni] = a[i]
print(n - len(seq))