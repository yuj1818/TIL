import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a = Counter(map(int, input().split()))
print('Yes' if a[2] <= a[1] and (a[2] * 2 + a[1]) % 3 == 0 else 'No')