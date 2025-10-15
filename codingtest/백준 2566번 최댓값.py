import sys
input = sys.stdin.readline
nums = [list(map(int, input().split())) for _ in range(9)]
ans = [-1, 0, 0]
for i in range(9):
    for j in range(9):
        if nums[i][j] > ans[0]:
            ans = [nums[i][j], i + 1, j + 1]
print(ans[0])
print(ans[1], ans[2])