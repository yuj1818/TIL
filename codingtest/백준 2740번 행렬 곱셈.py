import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
_, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]
R = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        for z in range(m):
            R[x][y] += A[x][z] * B[z][y]
for i in R: print(' '.join(map(str, i)))