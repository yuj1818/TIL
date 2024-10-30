import sys
s = set(sys.stdin.readline())
for x in 'MOBIS':
    if x not in s:
        print('NO')
        break
else:
    print('YES')