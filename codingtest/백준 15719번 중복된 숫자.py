import sys
n = int(sys.stdin.readline())
t = sum(range(1, n))
a = list(map(int, input().split()))
cur = 0
tmp = ''

for x in a:
    if x.isdigit(): tmp += x
    else:
        cur += int(tmp)
        tmp = ''

if tmp: cur += int(tmp)
print(cur - t)