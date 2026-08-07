from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
counter = defaultdict(int)
for i in range(n):
    for j in range(n):
        t = A[i] + B[j]
        counter[t] += 1
ans = 0
for i in range(n):
    for j in range(n):
        t = C[i] + D[j]
        v = -1 * t
        if v in counter:
            ans += counter[v]
print(ans)