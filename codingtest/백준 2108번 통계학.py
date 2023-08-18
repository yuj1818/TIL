from sys import stdin
input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
counts = dict()
for n in nums:
    counts[n] = counts.get(n, 0) + 1
counts = sorted(counts.items(), key=lambda x: (x[1], -x[0]), reverse=True)
print(round(sum(nums) / N))
print(sorted(nums)[N // 2])
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    print(counts[1][0])
else:
    print(counts[0][0])
print(max(nums) - min(nums))