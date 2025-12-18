from itertools import permutations
import sys
input = sys.stdin.readline
colors = set(input().rstrip().split() + input().rstrip().split())
print('\n'.join(map(lambda x: ' '.join(x), sorted(set(permutations([*colors, *colors], 2))))))