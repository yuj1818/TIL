import sys
input = sys.stdin.readline
tc = 1
while 1:
    n = int(input())
    if n == 0: break
    a = {i:input().strip() for i in range(1, n + 1)}
    print(tc, a[sum(range(1, n + 1)) * 2 - sum([int(input().split()[0]) for _ in range(2 * n - 1)])])
    tc += 1