from itertools import permutations
n, m = map(int, open(0).read().split())
nums = [str(i) for i in range(1, n + 1)]
print('\n'.join(' '.join(a) for a in list(permutations(nums, m))))