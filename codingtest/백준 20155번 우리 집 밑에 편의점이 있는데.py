from collections import Counter
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
print(max(Counter(map(int, input().split())).values()))