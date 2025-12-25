import sys
input = sys.stdin.readline
a, b = input().strip(), input().strip()
la, lb = len(a), len(b)
arr = [[0] * (la + 1) for _ in range(lb + 1)]
for i in range(1, lb + 1):
    for j in range(1, la + 1):
        if b[i - 1] == a[j - 1]: arr[i][j] = arr[i - 1][j - 1] + 1
        else: arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(arr[-1][-1])