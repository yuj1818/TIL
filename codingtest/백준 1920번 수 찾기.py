def binary_search(s, e, t):
    mid = (s + e) // 2
    if s == e:
        return 0
    if t == nums[mid]:
        return 1
    if t < nums[mid]:
        return binary_search(s, mid, t)
    if t > nums[mid]:
        return binary_search(mid + 1, e, t)
    return 0
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
for n in list(map(int, input().split())):
    print(binary_search(0, N, n))