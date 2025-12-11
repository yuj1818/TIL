import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
total = sum(a)
ans = 0
for x in a:
    total -= x
    ans += x * total
print(ans)