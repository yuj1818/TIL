import sys
n = int(input())
for i in range(n): sys.stdout.write(' ' * (n-i-1) + '*' * (i*2+1) + '\n')