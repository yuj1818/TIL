from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
A = sorted(Counter(map(int, input().split())).items(), key=lambda x:-x[1])
if A[0][0] == 0: A.pop(0)
if A[0][1] == A[1][1]: print('skipped')
else: print(A[0][0])