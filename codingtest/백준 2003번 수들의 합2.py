import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
acc = A[0]
s, e = 0, 1
while 1:
    if acc < m:
        if e == n: break
        acc += A[e]
        e += 1
    elif acc == m:
        cnt += 1
        acc -= A[s]
        s += 1
    else:
        acc -= A[s]
        s += 1
print(cnt)