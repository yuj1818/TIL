import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
rate = [x * n / 100 for x in [4, 11, 23, 40, 60, 77, 89, 96, 100]]
s = 0
ans = [0] * 9
for i in range(9):
    if s == n:
        break
    while s < n and s < rate[i]:
        ans[i] += 1
        s += 1
    while s < n and arr[s] == arr[s - 1]:
        ans[i] += 1
        s += 1
print(*ans, sep='\n')