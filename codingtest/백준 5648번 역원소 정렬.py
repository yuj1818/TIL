import sys
n, *a = [int(x[::-1]) for l in sys.stdin.readlines() for x in l.rstrip().split()]
print('\n'.join(map(str, sorted(a))))
