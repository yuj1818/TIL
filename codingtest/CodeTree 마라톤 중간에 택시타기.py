n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
L = [0] * n
R = [0] * n
for i in range(1, n):
    y1, x1 = points[i - 1]
    y2, x2 = points[i]
    L[i] = L[i - 1] + abs(y2 - y1) + abs(x2 - x1)
for i in range(n - 2, -1, -1):
    y1, x1 = points[i + 1]
    y2, x2 = points[i]
    R[i] = R[i + 1] + abs(y2 - y1) + abs(x2 - x1)
ans = float('inf')
for i in range(1, n - 1):
    y1, x1 = points[i + 1]
    y2, x2 = points[i - 1]
    ans = min(L[i - 1] + R[i + 1] + abs(y2 - y1) + abs(x2 - x1), ans)
print(ans)
