from math import ceil
import sys
n=int(sys.stdin.readline())
a=0
for i in range(ceil(n/3), (n-1)//2+1):
    a+=(n-i)//2+2*i-n+1
print(a)