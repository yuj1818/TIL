N = int(input())
answer = 0
max_num = 0
for i in range(N + 1):
    nums = [N, i]
    while nums[-2] - nums[-1] >= 0:
        nums.append(nums[-2] - nums[-1])
    if len(nums) > max_num:
        max_num = len(nums)
        answer = nums
print(max_num)
print(*answer)