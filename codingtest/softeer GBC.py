import sys
input = sys.stdin.readline
n, m = map(int, input().split())
limit = []
for _ in range(n):
    l, v = map(int, input().split())
    limit += [v] * l
ans = 0
cur = 0
for _ in range(m):
    l, v = map(int, input().split())
    for i in range(cur, cur + l):
        if v - limit[i] > ans:
            ans = v - limit[i]
    cur += l
print(ans)