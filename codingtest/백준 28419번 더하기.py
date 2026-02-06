import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
odd, even = 0, 0
for i in range(n):
    if i % 2:
        even += a[i]
    else:
        odd += a[i]
if n == 3 and odd > even:
    print(-1)
else:
    print(abs(odd - even))
