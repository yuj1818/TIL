import sys
input = sys.stdin.readline
input()
nums = sorted(map(int, input().split()))
print(nums[0] * nums[-1])