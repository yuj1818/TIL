import sys
input = sys.stdin.readline

def bs(s, e, t):
    while s < e:
        mid = (s + e) // 2
        if t > seq[mid]: s = mid + 1
        else: e = mid
    return e

n = int(input())
a = list(map(int, input().split()))
seq = [a[0]]
for i in range(1, n):
    if a[i] > seq[-1]:
        seq.append(a[i])
    else:
        ni = bs(0, len(seq) - 1, a[i])
        seq[ni] = a[i]
print(len(seq))