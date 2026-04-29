n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        acc[i][j] = acc[i][j - 1] + board[i - 1][j - 1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total = 0
        for y in range(i - k, i + k + 1):
            d = k - abs(i - y)
            if 0 < y <= n:
                total += acc[y][min(j + d, n)] - acc[y][max(j - d - 1, 0)]
        if ans < total: ans = total
print(ans)
