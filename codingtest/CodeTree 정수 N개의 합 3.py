n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + arr[i - 1][j - 1]

for i in range(k, n + 1):
    for j in range(k, n + 1):
        v = acc[i][j] - acc[i][j - k] - acc[i - k][j] + acc[i - k][j - k]
        ans = max(ans, v)
print(ans)
