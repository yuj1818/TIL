import sys
n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for _ in range(n)]
s = set(a)
for x in a:
    if x[::-1] in s:
        l = len(x)
        print(l, x[l // 2])
        exit()