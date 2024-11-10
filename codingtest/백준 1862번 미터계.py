import sys
n = list(map(int, sys.stdin.readline().strip()))
ans = 0
for i in range(1, len(n) + 1):
    if n[-i] > 4: n[-i] -= 1
    ans += n[-i] * 9 ** (i - 1)
print(ans)