n = int(input())
arr = list(map(int, input().split()))
L = [0] * n
R = [0] * n
for i in range(n):
    L[i] = max(L[i - 1], arr[i])
R[-1] = arr[-1]
for i in range(n - 2, -1, -1):
    R[i] = max(R[i + 1], arr[i])
ans = 0
for i in range(2, n - 2):
    ans = max(ans, L[i - 2] + arr[i] + R[i + 2])
print(ans)
