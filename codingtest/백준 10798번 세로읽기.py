import sys
a = [sys.stdin.readline().strip().ljust(15, ' ') for _ in range(5)]
for z in zip(*a):
    x = ''.join(z).replace(' ','')
    if not x: break
    sys.stdout.write(x)