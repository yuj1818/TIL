import sys
n = list(map(int, sys.stdin.readline().split()))
pre = n[0]
for x in n:
    if abs(x - pre) > 1:
        print('mixed')
        sys.exit()
    else:
        pre = x
print('ascending' if n[-1] == 8 else 'descending')