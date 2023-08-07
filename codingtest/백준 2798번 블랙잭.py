from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0
for comb in combinations(nums, 3):
    SUM = sum(comb)
    if max_sum < SUM <= M:
        max_sum = SUM
print(max_sum)
