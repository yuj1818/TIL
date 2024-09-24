import sys
input = sys.stdin.readline

n = int(input())
cookies = [0] * 5
grid = [input().rstrip() for _ in range(n)]
hy, hx = 0, 0
for i in range(n):
    if grid[i].count('*') == 1:
        hy, hx = i + 1, grid[i].index('*')
        break

for i in range(hy + 1, n):
    cookies[2] += 1 if grid[i][hx] == '*' else 0
    cookies[3] += 1 if grid[i][hx-1] == '*' else 0
    cookies[4] += 1 if grid[i][hx+1] == '*' else 0

for i in range(hx - 1, -1, -1):
    if grid[hy][i] == '*': cookies[0] += 1
    else: break

for i in range(hx + 1, n):
    if grid[hy][i] == '*': cookies[1] += 1
    else: break

print(hy + 1, hx + 1)
print(*cookies)