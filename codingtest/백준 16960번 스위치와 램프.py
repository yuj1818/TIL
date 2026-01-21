import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [0] * (m + 1)
l[0] = 1
s = [[]]
for i in range(n):
    _, *a = map(int, input().split())
    s.append(a)
    for x in a: l[x] += 1
if 0 in l: print(0)
else:
    for i in range(1, n + 1):
        for x in s[i]:
            if l[x] - 1 == 0: break
        else:
            print(1)
            break
    else: print(0)