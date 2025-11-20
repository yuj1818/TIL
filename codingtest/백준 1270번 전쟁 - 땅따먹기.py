import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    ti, *arr = input().rstrip().split()
    arr = sorted(Counter(arr).items(), key=lambda x: -x[1])
    print(arr[0][0] if arr[0][1] > (int(ti) / 2) else 'SYJKGW')