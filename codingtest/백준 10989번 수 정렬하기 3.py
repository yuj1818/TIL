import sys
input = sys.stdin.readline
N = int(input())
nums = dict()
for _ in range(N):
    n = int(input())
    nums[n] = nums.get(n, 0)
    nums[n] += 1
for n, cnt in sorted(nums.items()):
    for i in range(cnt):
        print(n)