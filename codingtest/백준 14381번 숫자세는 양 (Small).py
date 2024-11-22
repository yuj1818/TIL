import sys
input = sys.stdin.readline
for t in range(1, int(input()) + 1):
    n = int(input())
    if n == 0:
        print(f'Case #{t}: INSOMNIA')
        continue
    nums = set()
    i = 0
    while len(nums) < 10:
        i += 1
        for x in list(map(int, str(n * i))):
            nums.add(x)
    print(f'Case #{t}: {n * i}')