import sys
input = sys.stdin.readline
s = set()
for _ in range(28): s.add(int(input()))
print('\n'.join(map(str, sorted(set(range(1, 31)) - s))))