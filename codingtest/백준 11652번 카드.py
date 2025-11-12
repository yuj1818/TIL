import sys
input = sys.stdin.readline
n = int(input())
C = dict()
for _ in range(n):
    x = int(input())
    if x in C: C[x] += 1
    else: C[x] = 1
print(sorted(C.items(), key=lambda x: (-x[1], x[0]))[0][0])