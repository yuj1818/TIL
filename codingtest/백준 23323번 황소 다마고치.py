import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    while n > 0:
        n //= 2
        ans += 1
    print(ans + m)