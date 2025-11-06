import sys
input = sys.stdin.readline
n = int(input())
rope = sorted([int(input()) for _ in range(n)])
ans = rope[-1]
for i in range(n - 1):
    v = rope[i] * (n - i)
    if v > ans: ans = v
print(ans)