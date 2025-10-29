import sys
input = sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multiply(a, b):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            x = 0
            for z in range(N):
                x += a[i][z] * b[z][j]
            res[i][j] = x % 1000
    return res

def calc(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    cur = calc(A, B // 2)
    if B % 2:
        return multiply(multiply(cur, cur), A)
    else:
        return multiply(cur, cur)

ans = calc(A, B)
for row in ans:
    print(' '.join(map(str, row)))