N = int(input())
B = [input() for _ in range(N)]
L = [0] * N
R = [0] * N
for x in 'HSP':
    cnt = 0
    for i in range(N):
        if B[i] == x: cnt += 1
        L[i] = max(cnt, L[i])
    cnt = 0
    for i in range(N - 1, -1, -1):
        if B[i] == x: cnt += 1
        R[i] = max(cnt, R[i])
ans = 0
for i in range(N - 1):
    ans = max(ans, L[i] + R[i + 1])
print(ans)
