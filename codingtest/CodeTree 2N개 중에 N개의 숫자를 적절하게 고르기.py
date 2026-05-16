from itertools import combinations
n = int(input())
nums = list(map(int, input().split()))
ans = float('inf')
for comb in combinations(range(2 * n), n):
    a, b = 0, 0
    idx = 0
    for i in range(2 * n):
        if idx < n and comb[idx] == i:
            a += nums[i]
            idx += 1
        else: b += nums[i]
    ans = min(ans, abs(a - b))
print(ans)
