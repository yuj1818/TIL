import sys

def bis(s, e, x):
    while s <= e:
        m = (s + e) // 2
        if seq[m] >= x: e = m - 1
        else: s = m + 1
    return s

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
seq = [0]
for i in range(n):
    tmp = bis(0, len(seq) - 1, a[i])
    if tmp >= len(seq): seq.append(a[i])
    else: seq[tmp] = a[i]
print(len(seq) - 1)