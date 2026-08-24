from itertools import combinations
n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
ans = 0
for i, j, k in list(combinations(range(m), 3)):
    sa, sb = set(), set()
    for idx in range(n):
        sa.add(A[idx][i] + A[idx][j] + A[idx][k])
        sb.add(B[idx][i] + B[idx][j] + B[idx][k])
    if sa & sb: continue
    ans += 1
print(ans)