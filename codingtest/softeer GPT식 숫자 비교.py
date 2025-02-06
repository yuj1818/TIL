import sys
n = int(input())
nums = []
for _ in range(n):
    x, *y = map(int, input().split('.'))
    nums.append([x, y[0] if y else -1])
nums.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    if nums[i][1] >= 0:
        print('.'.join(map(str, nums[i])))
    else: print(nums[i][0])