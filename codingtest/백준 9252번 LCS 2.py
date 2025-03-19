import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()
matrix = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if b[i - 1] == a[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
print(matrix[-1][-1])
ans = ''
y, x = len(b), len(a)
while y > 0 and x > 0:
    if b[y - 1] == a[x - 1]:
        ans = a[x - 1] + ans
        y -= 1
        x -= 1
    elif matrix[y - 1][x]  >= matrix[y][x - 1]: y -= 1
    else: x -= 1
sys.stdout.write(ans)