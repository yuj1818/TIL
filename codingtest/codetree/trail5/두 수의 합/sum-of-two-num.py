from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = Counter(arr)
nums = sorted(d.keys())
s, e = 0, len(nums) - 1
cnt = 0
while s < e:
    if nums[s] + nums[e] == k:
        cnt += d[nums[s]] * d[nums[e]]
        e -= 1
        s += 1
    elif nums[s] + nums[e] > k: e -= 1
    else: s += 1
if s == e and nums[e] * 2 == k:
    cnt += int(d[nums[e]] * (d[nums[e]] - 1) / 2)
print(cnt)