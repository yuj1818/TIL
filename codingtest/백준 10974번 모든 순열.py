from itertools import permutations
n = int(input())
for p in sorted(permutations(range(1, n + 1), n)): print(' '.join(map(str, p)))
