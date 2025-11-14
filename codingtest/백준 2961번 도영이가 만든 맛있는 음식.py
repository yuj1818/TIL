import sys
input = sys.stdin.readline
n = int(input())
I = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
for i in range(1, 1 << n):
    s, b = 1, 0
    for j in range(n):
        if i & (1 << j):
            s *= I[j][0]
            b += I[j][1]
    ans = min(ans, abs(s - b))
print(ans)