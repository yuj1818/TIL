import sys
input = sys.stdin.readline
N, M, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for _ in range(Q):
    c, i, j, *k = map(int, input().split())
    if c == 0: A[i][j] = k[0]
    else: A[i], A[j] = A[j], A[i]
for i in range(N): print(' '.join(map(str, A[i])))