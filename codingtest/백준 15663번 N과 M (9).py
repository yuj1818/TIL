from itertools import permutations
n, m = map(int, input().split())
nums = sorted(input().split(), key=int)
print('\n'.join((' '.join(arr) for arr in dict.fromkeys(permutations(nums, m)).keys())))