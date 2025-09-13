import sys, math
input = sys.stdin.readline
m, n = int(input()), int(input())
arr = [i ** 2 for i in range(math.ceil(m ** 0.5), int(n ** 0.5) + 1)]
if arr: print(f'{sum(arr)}\n{arr[0]}')
else: print(-1)