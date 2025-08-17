import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n == 0: break
    h = []
    for _ in range(n):
        k, v = input().strip().split()
        h.append((k, float(v)))
    h.sort(key=lambda x: -x[1])
    for i in range(n):
        if h[i][1] == h[0][1]: print(h[i][0], end=' ')
    print()