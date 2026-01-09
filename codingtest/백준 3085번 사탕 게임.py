import sys
input = sys.stdin.readline
n = int(input())
colors = [list(input().rstrip()) for _ in range(n)]
ans = 0

def check():
    global ans
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if colors[i][j] == colors[i][j + 1]:
                cnt += 1
                ans = max(ans, cnt)
            else: cnt = 1
    for j in range(n):
        cnt = 1
        for i in range(n - 1):
            if colors[i][j] == colors[i + 1][j]:
                cnt += 1
                ans = max(ans, cnt)
            else: cnt = 1

for i in range(n):
    for j in range(n - 1):
        colors[i][j], colors[i][j + 1] = colors[i][j + 1], colors[i][j]
        check()
        colors[i][j + 1], colors[i][j] = colors[i][j], colors[i][j + 1]
        colors[j][i], colors[j + 1][i] = colors[j + 1][i], colors[j][i]
        check()
        colors[j + 1][i], colors[j][i] = colors[j][i], colors[j + 1][i]
print(ans)