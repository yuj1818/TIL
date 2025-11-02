import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    if len(arr) == 2: break
    r = list(map(int, input().split()))
    for j in range(m):
        if len(arr) == 2: break
        if r[j]: arr.append((i, j))
print(abs(arr[1][0] - arr[0][0]) + abs(arr[1][1] - arr[0][1]))