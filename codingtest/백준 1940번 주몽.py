import sys
input = sys.stdin.readline
n, m = int(input()), int(input())
A = sorted(map(int, input().split()))
ans, s, e = 0, 0, n - 1
while s < e:
    x = A[s] + A[e]
    if x == m:
        ans += 1
        s += 1
        e -= 1
    elif x < m: s += 1
    else: e -= 1
print(ans)