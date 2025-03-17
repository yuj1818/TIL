import sys
input = sys.stdin.readline
n = int(input())
s = [input().strip() for _ in range(n)]
tidx = s.index('?')
ts = s[tidx - 1][-1] if tidx > 0 else ''
te = s[tidx + 1][0] if tidx < n - 1 else ''
m = int(input())
for _ in range(m):
    x = input().strip()
    if x not in s and (x[0] == ts if ts else True) and (x[-1] == te if te else True):
        print(x)
        sys.exit()